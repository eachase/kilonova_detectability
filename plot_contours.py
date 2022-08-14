#!/usr/bin/env python

__author__ = 'Eve Chase <eachase@lanl.gov>'

from astropy import units as u
from astropy.cosmology import Planck18_arXiv_v2, z_at_value
import argparse
import collections
import glob
import numpy as np
import pandas as pd
from scipy.signal import savgol_filter


# Matplotlib settings
import matplotlib
matplotlib.rcParams['figure.figsize'] = (12, 8.0)
matplotlib.rcParams['xtick.labelsize'] = 24.0
matplotlib.rcParams['ytick.labelsize'] = 24.0
matplotlib.rcParams['axes.titlesize'] = 27.0
matplotlib.rcParams['axes.labelsize'] = 27.0
matplotlib.rcParams['legend.fontsize'] = 24.0
matplotlib.rcParams['text.usetex'] = True
matplotlib.rcParams['text.latex.preamble'] = r"\usepackage{amsmath}"
matplotlib.rcParams['font.serif'] = ['Computer Modern', 'Times New Roman']
matplotlib.rcParams['font.family'] = ['serif', 'STIXGeneral']
matplotlib.rcParams['legend.frameon'] = True
import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1 import make_axes_locatable, axes_size

# Local imports
from cocteau import matrix, observations, filereaders
from cocteau import observational_utils as utils

# Some custom titles
band_titles = {
    'RomanR': r'Roman/$\textit{R}$-band',
    'RomanZ': r'Roman/$\textit{Z}$-band',
    'RomanY': r'Roman/$\textit{Y}$-band',
    'RomanJ': r'Roman/$\textit{J}$-band',
    'RomanH': r'Roman/$\textit{H}$-band',
    'RomanF': r'Roman/$\textit{F}$-band',
    'ZTF_g' : r'ZTF/$\textit{g}$-band',
    'ZTF_r' : r'ZTF/$\textit{r}$-band',
    'ZTF_i' : r'ZTF/$\textit{i}$-band',
    'u-band': r'LSST/$\textit{u}$-band',
    'g-band': r'LSST/$\textit{g}$-band',
    'r-band': r'LSST/$\textit{r}$-band',
    'i-band': r'LSST/$\textit{i}$-band',
    'z-band': r'LSST/$\textit{z}$-band',
    'y-band': r'LSST/$\textit{y}$-band',
    'Dorado': r'Dorado/$\textit{NUV}_D$',
    'g-bg':   r'$\textit{g}$-band',
    'i-bg':   r'$\textit{i}$-band',
    'r-bg':   r'$\textit{r}$-band',
    'u-bg':   r'$\textit{u}$-band',
    'z-bg':   r'$\textit{z}$-band',
    'vr-bg':   r'$\textit{q}$-band',
    'DECam_i':r'DECam/$\textit{i}$-band',
    'DECam_z':r'DECam/$\textit{z}$-band',
    'ULTRASAT': r'ULTRASAT/$\textit{NUV}$',
    'w-band': r'DDOTI/$\textit{w}$-band',
    'VistaY': r'VISTA/$\textit{Y}$-band',
    'VistaJ': r'VISTA/$\textit{J}$-band',
    'VistaKs': r'VISTA/$\textit{K}_s$-band',
    'VistaZ': r'VISTA/$\textit{Z}$-band',
    'VistaH': r'VISTA/$\textit{H}$-band',
    'PrimeH': r'PRIME/$\textit{H}$-band',
    'PrimeZ': r'PRIME/$\textit{Z}$-band',
    'PrimeJ': r'PRIME/$\textit{J}$-band',
    'PrimeY': r'PRIME/$\textit{Y}$-band',
    'GOTO': r'GOTO/$\textit{L}$-band',
    'WinterY': r'WINTER/$\textit{Y}$-band',
    'WinterJ': r'WINTER/$\textit{J}$-band',
    'WinterH': r'WINTER/$\textit{H}_s$-band',
    'Gamow0': r'Gamow (5000 - 6400 $\mathrm{\AA}$)',
    'Gamow1': r'Gamow (6400 - 8700 $\mathrm{\AA}$)',
    'Gamow2': r'Gamow (8700 - 12,000 $\mathrm{\AA}$)',
    'Gamow3': r'Gamow (12,000 - 17,000 $\mathrm{\AA}$)',
    'Gamow4': r'Gamow (17,000 - 24,000 $\mathrm{\AA}$)',
    'RAPTOR': r'RAPTOR (4000 - 10,000 $\mathrm{\AA}$)',
    'F560W': r'JWST/MIRI/F560W',
    'F770W': r'JWST/MIRI/F770W',
    'F1000W': r'JWST/MIRI/F1000W',
    'F1130W': r'JWST/MIRI/F1130W',
    'F1280W': r'JWST/MIRI/F1280W',
    'F1500W': r'JWST/MIRI/F1500W',
    'F1800W': r'JWST/MIRI/F1800W',
    'F2100W': r'JWST/MIRI/F2100W',
    'F2550W': r'JWST/MIRI/F2550W',
    'U-band': r'Swift/$\textit{U}$-band',
    'B-band': r'Swift/$\textit{B}$-band',
    'UVM2'  : r'Swift/UVM2',
    'UVW1'  : r'Swift/UVW1',
    'UVW2'  : r'Swift/UVW2',
    'GenericU'  : r'Generic $\textit{u}$-band',
    'GenericI'  : r'Generic $\textit{i}$-band',
    'GenericK'  : r'Generic $\textit{K}$-band',
}



def fraction_detected(data_dict, lim_mags, redshift,
    time=None, param_restrict=None):
 

    # Pre-compute redshift and distance factors   
    redshift_factor = 1 + redshift
    dist_lum = Planck18_arXiv_v2.luminosity_distance(redshift)

    # Set up data frame for detections
    overall_detectability = None

    for idx, (band, band_data) in enumerate(data_dict.items()):

        if redshift in band_data.keys():
            data_at_z = band_data[redshift]

            # Store data files
            magmatrix = pd.read_pickle(data_at_z['magmatrix'])
            knprops = pd.read_pickle(data_at_z['knprops'])
            times = pd.read_pickle(data_at_z['times'])

            # Redshift the times
            times *= redshift_factor

            # Convert absolute magnitudes to apparent
            magmatrix = utils.appMag(magmatrix, dist_lum)

            # Restrict to parameters of interest
            if param_restrict is not None:
                valid_idx = knprops.index.values
                for param, param_vals in param_restrict.items():
                    valid_idx = np.intersect1d(valid_idx,
                        knprops[knprops[param].isin(
                        param_vals)].index.values)
                
                # Update existing data frames
                magmatrix = magmatrix.loc[valid_idx]
                knprops = knprops.loc[valid_idx]
                times = times.loc[valid_idx]

            # Create a new magmatrix object
            magmatrix = matrix.MagMatrix(magmatrix, times=times,
                knprops=knprops)

            # Find time closest to the time in question
            times = np.unique(magmatrix.times.values)
            closest_time_idx = np.argmin(np.fabs(times - time))
            time_idx_arr = [closest_time_idx]
            closest_times = [times[closest_time_idx]]
            # FIXME: actually try to get this to work?
            #try:
            #    closest_times.append(times[closest_time_idx+1])
            #    time_idx_arr.append(closest_time_idx + 1)
            #except:
            #    pass

            detectable_df = magmatrix.matrix.loc(
                axis=0)[:, time_idx_arr] < lim_mags[idx]

            # Ok this is actually very confusing
            # Prettymuch I combine the previous detectability
            # statement with a new detectability matrix and check
            # to see if the light curve is detectable with any
            # light curve
            if overall_detectability is None:
                overall_detectability = detectable_df
            else:
                assert overall_detectability.shape == \
                    detectable_df.shape
                overall_detectability = \
                    overall_detectability.combine(
                    detectable_df.rename(
                    columns={detectable_df.columns[0]: \
                    overall_detectability.columns[0]}),
                    np.maximum)



    num_det = np.where(overall_detectability.groupby(
        level=0).sum().values.flatten() > 0)[0].shape[0]
    num_lc = magmatrix.knprops.shape[0]

    print(redshift, time, num_det / num_lc, num_det, num_lc)
    return num_det / num_lc





def plot_contours(bands, num_timesteps=10, 
    lim_mags=[25], instr_list=['VRO'], data_dir='./',
    max_z=None, param_restrict=None, custom_title=None,
    legend=False, plot=True):
    
    if max_z is None:
        max_z = np.inf

    # Identify available data
    data_dict = {}
    redshifts = np.array([])
    for idx, band in enumerate(bands):
        instr = instr_list[idx]
        data_dict_band = {}

        if instr == 'MeerLICHT':
            instr_plot = 'BlackGEM'
        else:
            instr_plot = instr

        for magmatrix_file in glob.glob(
            f'{data_dir}{instr_plot}/*/magmatrix_{band}*pkl'):

            redshift = float(
                magmatrix_file.split('/')[-2].split('_')[-1])

            if redshift <= max_z:
                data_dict_band[redshift] = {
                    'magmatrix': magmatrix_file,
                    'knprops': magmatrix_file.replace(
                        'magmatrix', 'knprops'),
                    'times': magmatrix_file.replace(
                        'magmatrix', 'times')
            }

        # Created ordered dictionary based on redshift
        data_dict_band = collections.OrderedDict(
            sorted(data_dict_band.items()))

        data_dict[band] = data_dict_band


        # Construct redshift array from data 
        if redshifts.shape[0] > 1:
            redshifts = np.intersect1d(redshifts,
                np.asarray(sorted(data_dict_band.keys())))
        else:
            redshifts = np.asarray(sorted(data_dict_band.keys()))

    print(redshifts)

    # Set up timing array for plotting
    redshift_factor = (1 + np.max(redshifts))
    min_time = 0.125 * redshift_factor
    max_time = 20 * redshift_factor #min(20, 4 + 20*np.max(redshifts))  #min(20, 26.909 * redshift_factor)
    print('Minimum timestep:', min_time)
    times_arr = np.logspace(np.log10(min_time), 
        np.log10(max_time), num_timesteps)
    
    detectability_data = {}

    # FIXME: this is particularly bad code etiquette
    for redshift in redshifts:
        print(redshift)
        detectability_data[redshift] = [fraction_detected(
            data_dict, lim_mags, redshift, time=time, 
            param_restrict=param_restrict) for time in times_arr]
        
    X, Y = np.meshgrid(times_arr, redshifts)
    Z = np.zeros_like(X)

    # Structure the contour output
    for z_idx, (redshift, band_data) in enumerate(
        detectability_data.items()):
        for time_idx, time in enumerate(times_arr):
            Z[z_idx, time_idx] = band_data[time_idx]


    fig, ax = plt.subplots(dpi=100, linewidth=2)
    levels = np.linspace(0, 1, 150)
    contour = ax.contourf(X, Y, Z, cmap='inferno', levels=levels)
    ax.set_ylabel('Redshift')
    ax.set_xscale('log')
    ax.set_xlabel('Observer-Frame Time (d)')
    
    xtick_vals = [0.25, 0.5, 1, 2, 4, 8, 16, 32]
    ax.set_xticks(xtick_vals)
    ax.set_xticklabels(xtick_vals)
    ax.set_xlim(min_time, max_time)
    ax.minorticks_off()

    zmin = np.min(redshifts)
    zmax = np.max(redshifts)

    ax.set_ylim(zmin, zmax)
       


    # Second y axis for luminosity distance
    ax2 = ax.twinx()
    if zmax < 0.2:
        dist_arr = [10, 50, 100, 200, 300, 400, 500, 600, 700]
        u_dist = u.Mpc
    elif zmax <= 0.6:
        dist_arr = [0.1, 0.5, 1, 1.5, 2, 2.5, 
            3, 3.5, 4]
        u_dist = u.Gpc
    elif zmax <= 1.0:
        dist_arr = np.concatenate((np.array([0.1]), 
            np.arange(1, 20, 1)))
        u_dist = u.Gpc
    else:
        dist_arr = np.concatenate((np.array([0.1, 1]), 
            np.arange(2, 20, 2)))
        u_dist = u.Gpc

    ax2.set_yticks([z_at_value(
        Planck18_arXiv_v2.luminosity_distance, 
        dist * u_dist) for dist in dist_arr])
    ax2.set_yticklabels(dist_arr)
    ax2.set_ylim(zmin, zmax)
    if u_dist == u.Gpc:
        ax2.set_ylabel(r'Luminosity Distance $\left[\mathrm{Gpc}\right]$')
    elif u_dist == u.Mpc:
        ax2.set_ylabel(r'Luminosity Distance $\left[\mathrm{Mpc}\right]$')



    norm = matplotlib.colors.Normalize(vmin=0, vmax=1)
    sm = plt.cm.ScalarMappable(norm=norm, cmap=contour.cmap)
    sm.set_array([])
    fig.colorbar(sm, ticks=np.linspace(0, 1, 6), 
        label='Fraction Detectable', pad=0.125)

    #contour_levels = [0.01, 0.1, 0.5]
    #contour_levels = [0.1, 0.5, 0.9]
    if instr == 'SIBEX':
        contour_levels = [0.1, 0.5, 0.9]
    else:
        contour_levels = [0.05, 0.5, 0.95]
    contour_levels_rev = contour_levels[::-1]
    contour_thresh = ax.contour(X, Y, Z, levels=contour_levels, colors='0.75', alpha=0)

    ls_arr = ['solid', 'dashdot', 'dotted', 'dashed']
    count = 0
    contour_data_bylevel = {}
    for idx, collection in enumerate(contour_thresh.collections):

        ls = ls_arr.pop()
        level = contour_levels[idx]
        contour_data_bylevel[level] = []

        for path in collection.get_paths():
            contour_data = path.vertices[::-1]
            contour_data_bylevel[level].append(contour_data)

            print(contour_data[:,0].shape)
            if contour_data[:,0].shape[0] > 2:
                try:
                    smooth_interp = savgol_filter(contour_data[:,1], 17, 3)
                except:
                    try:
                        smooth_interp = savgol_filter(contour_data[:,1], 11, 3)
                    except:
                        try:
                            smooth_interp = savgol_filter(contour_data[:,1], 3, 1)
                        except:
                            ax.set_title('Failed')
                        
                ax.plot(contour_data[:,0], smooth_interp, 
                    lw=5, ls=ls, color='0.75', label=f'{level}')

        # Report maximum z for each percentile curve
        max_z = np.max(contour_data[:,1])
        print(level, max_z)

        # Set title
        if level == 0.5:

            if custom_title is not None:
                ax.set_title(custom_title)

            else:

                try:
                    #ax.axhline(y=max_z, c='r', ls='-.')
                    if instr == 'SIBEX':
                        ax.set_title(f'{instr}: ' + r'$m_{\mathrm{lim}}$' + f' = {lim_mags[0]}') 
                    #elif band == instr:
                    #    ax.set_title(f'{instr}: z = {max_z:.2f}')
                    elif instr in ['BlackGEM', 'MeerLICHT']:
                        ax.set_title(f'{instr}/{band_titles[band]}')
                    elif band in band_titles:
                        ax.set_title(
                            f'{band_titles[band]}')
                    elif instr == 'Swift':
                         ax.set_title(
                            r'UVOT/$\textit{u}$-band')
                    else:
                        ax.set_title(
                            f'{instr}/{band}: z = {max_z:.2f}')
                    #ax.set_title(band)
                except:
                    ax.set_title(band)
                        
        count += 1

    if legend:
        ax.legend(loc='upper right', labelcolor='white', 
            facecolor='dimgray')

    if plot:
        return ax, contour_data_bylevel, min_time, max_time
    else:
        return contour_data_bylevel, min_time, max_time

if __name__ == '__main__':

    # Input parameters
    parser = argparse.ArgumentParser()

    # Base directory
    parser.add_argument('-d', '--data-dir', type=str,
        default='../../data/converted_lightcurves/')

    # Limiting magnitude
    parser.add_argument('-m', '--lim-mag', type=float, 
        default=[25], nargs='+')

    # Number of timesteps
    parser.add_argument('-n', '--num-timesteps', type=int, 
        #default=10)
        default=50)

    # Maximum redshift to plot
    parser.add_argument('-z', '--max-z', type=float, 
        default=None)

    # Instrument
    parser.add_argument('--instr', type=str, 
        default=['VRO'], nargs='+')

    # Filter
    parser.add_argument('-f', '--filter', type=str, 
        default=['r-band'], nargs='+')

    # Filter directory
    parser.add_argument('--filter-dir', type=str,
        default='data/filters/')

    # Title for plot
    parser.add_argument('-t', '--title', type=str, default=None)

    # Include legend
    parser.add_argument('--legend', default=True, action='store_true')
    parser.add_argument('--no-legend', dest='legend', action='store_false')

    # Add in AT2017gfo detectability data
    parser.add_argument('--gw170817', default=False, action='store_true')

    # Parameters to restrict
    parser.add_argument('--param', type=str, default=None,
        nargs='+')

    # Values to restrict parameters to
    parser.add_argument('--paramvals', type=str, default=None,
        nargs='+')

    # Output directory
    parser.add_argument('-o', '--out-dir', type=str, 
        default='figures/contours/')

    args = parser.parse_args()

    # Check that filters input correctly
    num_filters = len(args.instr)
    assert num_filters == len(args.filter)
    assert num_filters == len(args.lim_mag)

    # Set up dictionary of parameters to restrict study to
    if args.param is None or args.paramvals is None:
        param_restrict = None
    else:
        param_restrict = {}
        for idx, param in enumerate(args.param):
            param_restrict[param] = [float(i) for i in \
            args.paramvals[idx].strip('][').split(', ')]

    # Read band
    bandname = args.filter[0]
    filetype, instr, filename = filereaders.band_files[bandname]
    filename = f'{args.filter_dir}{filename}'

    if filetype == 'norm':
        fr = filereaders.FileReader()
        band = fr.read_band(filename,
            bandname=bandname, wl_units=u.Angstrom)
    elif filetype == 'tab':
        fr = filereaders.TabFileReader()
        band = fr.read_band(filename,
            bandname=bandname, wl_units=u.Angstrom)

    # Report effective wavelength
    print(bandname, band.effective_wavelength().to(u.Angstrom))    


    # Compute AT2017gfo detectability
    plot_gw170817 = False
    if args.gw170817:
        print('Adding AT2017gfo data')

        # Compute contour for AT2017gfo detectability in band
        times, max_z = utils.compute_at2017gfo(
            data_file='data/GW170817.json', band=band,
            lim_mag=args.lim_mag[0])
        if max_z is not None:
            plot_gw170817 = True

    ax, _, _, _ = plot_contours(args.filter, 
        num_timesteps=args.num_timesteps, 
        lim_mags=args.lim_mag, instr_list=args.instr, 
        data_dir=args.data_dir, max_z=args.max_z,
        param_restrict=param_restrict,
        custom_title=args.title, legend=args.legend)

    # Add in AT2017gfo observational data
    if plot_gw170817:
        # Add to figure
        ax.plot(times, max_z, lw=5, ls='-', color='magenta', 
            label=r'AT\,2017gfo')
        if args.legend:
            ax.legend(labelcolor='white', frameon=True, facecolor='dimgray')

    # Save figure
    filename = f'{args.out_dir}'
    if num_filters == 1:
        filename += f'{args.instr[0]}/{args.filter[0]}'
    else:
        filename += 'multiple/'
        for idx, band in enumerate(args.filter):
            if idx > 0:
                filename += '_'
            filename += f'{band}'
    # FIXME! add update to file name for params
    if param_restrict is not None:
        for param, paramvals in param_restrict.items():
            filename += f'_{param}'
            for val in paramvals:
                filename += f'_{val}'

    filename += '.png'
    print(filename)
    plt.savefig(filename)



