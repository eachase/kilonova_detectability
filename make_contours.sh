#!/bin/bash

# WINTER
python plot_contours.py --instr 'WINTER' -f 'WinterY' --lim-mag 21.5 --gw170817 -z 0.15
python plot_contours.py --instr 'WINTER' -f 'WinterJ' --lim-mag 21.3 --gw170817 -z 0.15
python plot_contours.py --instr 'WINTER' -f 'WinterH' --lim-mag 20.5 --gw170817 -z 0.15

# GOTO
python plot_contours.py --instr 'GOTO' -f 'GOTO' --lim-mag 21 --gw170817 -z 0.15

# PRIME
python plot_contours.py --instr 'PRIME' -f 'PrimeZ' --lim-mag 20.5 --gw170817 -z 0.1
python plot_contours.py --instr 'PRIME' -f 'PrimeY' --lim-mag 20.0 --gw170817 -z 0.1
python plot_contours.py --instr 'PRIME' -f 'PrimeJ' --lim-mag 19.6 --gw170817 -z 0.1
python plot_contours.py --instr 'PRIME' -f 'PrimeH' --lim-mag 18.4 --gw170817 -z 0.1

# VISTA
python plot_contours.py --instr 'VISTA' -f 'VistaZ' --lim-mag 22.0 -z 0.2 --gw170817
python plot_contours.py --instr 'VISTA' -f 'VistaY' --lim-mag 21.5 -z 0.2 --gw170817
python plot_contours.py --instr 'VISTA' -f 'VistaJ' --lim-mag 21.0 -z 0.2 --gw170817
python plot_contours.py --instr 'VISTA' -f 'VistaH' --lim-mag 21.0 -z 0.2 --gw170817
python plot_contours.py --instr 'VISTA' -f 'VistaKs' --lim-mag 20.0 -z 0.2 --gw170817


# ULTRASAT
python plot_contours.py --instr 'ULTRASAT' -f 'ULTRASAT' --lim-mag 22.3 -z 0.15

# DDOTI
python plot_contours.py --instr 'DDOTI' -f 'w-band' --lim-mag 20.5 -z 0.1


# DECam
python plot_contours.py --instr 'DECam' -f 'DECam_i' --lim-mag 22.5 --gw170817
python plot_contours.py --instr 'DECam' -f 'DECam_z' --lim-mag 21.8 --gw170817

# BlackGEM
python plot_contours.py --instr 'BlackGEM' -f 'u-bg' --lim-mag 21.5 -z 0.25 --gw170817
python plot_contours.py --instr 'BlackGEM' -f 'g-bg' --lim-mag 22.6 -z 0.25 --gw170817 
python plot_contours.py --instr 'BlackGEM' -f 'vr-bg' --lim-mag 23 -z 0.25 --gw170817
python plot_contours.py --instr 'BlackGEM' -f 'r-bg' --lim-mag 22.3 -z 0.25 --gw170817
python plot_contours.py --instr 'BlackGEM' -f 'i-bg' --lim-mag 21.8 -z 0.25 --gw170817
python plot_contours.py --instr 'BlackGEM' -f 'z-bg' --lim-mag 20.7 -z 0.25 --gw170817

# MeerLICHT
python plot_contours.py --instr 'MeerLICHT' -f 'u-bg' --lim-mag 19.06 -z 0.1 --gw170817
python plot_contours.py --instr 'MeerLICHT' -f 'g-bg' --lim-mag 20.2 -z 0.1 --gw170817
python plot_contours.py --instr 'MeerLICHT' -f 'vr-bg' --lim-mag 20.6 -z 0.1 --gw170817
python plot_contours.py --instr 'MeerLICHT' -f 'r-bg' --lim-mag 19.9 -z 0.1 --gw170817
python plot_contours.py --instr 'MeerLICHT' -f 'i-bg' --lim-mag 19.4 -z 0.1 --gw170817
python plot_contours.py --instr 'MeerLICHT' -f 'z-bg' --lim-mag 18.3 -z 0.1 --gw170817

# Swift
python plot_contours.py --instr 'Swift' -f 'U-band' -m 19.9 -z 0.1

# ZTF
python plot_contours.py --instr 'ZTF' -f 'ZTF_g' --lim-mag 20.8 -z 0.1 --gw170817
python plot_contours.py --instr 'ZTF' -f 'ZTF_r' --lim-mag 20.6 --gw170817 -z 0.1 --gw170817
python plot_contours.py --instr 'ZTF' -f 'ZTF_i' --lim-mag 19.9 --gw170817 -z 0.1 --gw170817

# VRO
python plot_contours.py --instr 'VRO' -f 'u-band' --lim-mag 23.57 -z 0.5
python plot_contours.py --instr 'VRO' -f 'g-band' --lim-mag 24.65 -z 0.5 --gw170817
python plot_contours.py --instr 'VRO' -f 'r-band' --lim-mag 24.21 -z 0.5 --gw170817 # figure in paper
python plot_contours.py --instr 'VRO' -f 'i-band' --lim-mag 23.79 -z 0.5 --gw170817
python plot_contours.py --instr 'VRO' -f 'z-band' --lim-mag 23.21 -z 0.5 --gw170817
python plot_contours.py --instr 'VRO' -f 'y-band' --lim-mag 22.31 -z 0.5 --gw170817

# Roman
python plot_contours.py --instr 'Roman' -f 'RomanR' --lim-mag 26.2 -z 1.0 --gw170817
python plot_contours.py --instr 'Roman' -f 'RomanZ' --lim-mag 25.7 -z 1.0 --gw170817
python plot_contours.py --instr 'Roman' -f 'RomanY' --lim-mag 25.6 -z 1.0 --gw170817
python plot_contours.py --instr 'Roman' -f 'RomanJ' --lim-mag 25.5 -z 1.0 --gw170817
python plot_contours.py --instr 'Roman' -f 'RomanF' --lim-mag 24.9 -z 1.0 --gw170817
python plot_contours.py --instr 'Roman' -f 'RomanH' --lim-mag 25.4 -z 1.0 --gw170817 #--no-legend # figure in paper


# Extra Roman figures for mass variability -- figures in paper
python plot_contours.py --instr 'Roman' -f 'RomanH' --lim-mag 25.4 --param 'md' --paramvals '[0.1]' --title 'Roman/$\textit{H}$-band:  $m_{\mathrm{dyn}} = 0.1 M_{\odot}$' --no-legend
python plot_contours.py --instr 'Roman' -f 'RomanH' --lim-mag 25.4 --param 'md' --paramvals '[0.001]' --title 'Roman/$\textit{H}$-band: $m_{\mathrm{dyn}} = 0.001 M_{\odot}$'
python plot_contours.py --instr 'Roman' -f 'RomanH' --lim-mag 25.4 --param 'mw' --paramvals '[0.1]' --title 'Roman/$\textit{H}$-band: $m_{\mathrm{wind}} = 0.1 M_{\odot}$' --no-legend
python plot_contours.py --instr 'Roman' -f 'RomanH' --lim-mag 25.4 --param 'mw' --paramvals '[0.001]' --title 'Roman/$\textit{H}$-band: $m_{\mathrm{wind}} = 0.001 M_{\odot}$' --no-legend

python plot_contours.py --instr 'Roman' -f 'RomanH' --lim-mag 25.4 --param 'mw' 'md' --paramvals '[0.001]' '[0.001]' --title 'Roman/$\textit{H}$-band: 0.002 $M_{\odot}$ total ejecta mass'
python plot_contours.py --instr 'Roman' -f 'RomanH' --lim-mag 25.4 --param 'mw' 'md' --paramvals '[0.1]' '[0.1]' --title 'Roman/$\textit{H}$-band: 0.2 $M_{\odot}$ total ejecta mass' --no-legend
python plot_contours.py --instr 'Roman' -f 'RomanH' --lim-mag 25.4 --param 'md' --paramvals '[0.01]' --title 'Roman/$\textit{H}$-band: $m_{\mathrm{dyn}} = 0.01 M_{\odot}$' --no-legend
python plot_contours.py --instr 'Roman' -f 'RomanH' --lim-mag 25.4 --param 'mw' --paramvals '[0.01]' --title 'Roman/$\textit{H}$-band: $m_{\mathrm{wind}} = 0.01 M_{\odot}$' --no-legend

