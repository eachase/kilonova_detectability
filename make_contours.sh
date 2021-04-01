#!/bin/bash

# Swift
python plot_contours.py --instr 'Swift' -f 'U-band' -m 19.9 -z 0.1

# ZTF
python plot_contours.py --instr 'ZTF' -f 'ZTF_g' --lim-mag 20.8 -z 0.15 --gw170817
python plot_contours.py --instr 'ZTF' -f 'ZTF_r' --lim-mag 20.6 --gw170817 -z 0.15 --gw170817
python plot_contours.py --instr 'ZTF' -f 'ZTF_i' --lim-mag 19.9 --gw170817 -z 0.1 --gw170817

# VRO
python plot_contours.py --instr 'VRO' -f 'u-band' --lim-mag 23.57 -z 0.5
python plot_contours.py --instr 'VRO' -f 'g-band' --lim-mag 24.65 -z 0.75 --gw170817
python plot_contours.py --instr 'VRO' -f 'r-band' --lim-mag 24.21 -z 1.0 --gw170817 # figure in paper
python plot_contours.py --instr 'VRO' -f 'i-band' --lim-mag 23.79 -z 0.6 --gw170817
python plot_contours.py --instr 'VRO' -f 'z-band' --lim-mag 23.21 -z 0.4 --gw170817
python plot_contours.py --instr 'VRO' -f 'y-band' --lim-mag 22.31 -z 0.25 --gw170817

# Roman
python plot_contours.py --instr 'Roman' -f 'RomanR' --lim-mag 26.2 --gw170817
python plot_contours.py --instr 'Roman' -f 'RomanZ' --lim-mag 25.7 --gw170817
python plot_contours.py --instr 'Roman' -f 'RomanY' --lim-mag 25.6 --gw170817
python plot_contours.py --instr 'Roman' -f 'RomanJ' --lim-mag 25.5 --gw170817
python plot_contours.py --instr 'Roman' -f 'RomanF' --lim-mag 24.9 --gw170817
python plot_contours.py --instr 'Roman' -f 'RomanH' --lim-mag 25.4 --gw170817 --no-legend # figure in paper


# Extra Roman figures for mass variability -- figures in paper
python plot_contours.py --instr 'Roman' -f 'RomanH' --lim-mag 25.4 --param 'md' --paramvals '[0.1]' --title 'Roman/$\textit{H}$-band: 0.1 $M_{\odot}$ low-$Y_e$ mass' --no-legend
python plot_contours.py --instr 'Roman' -f 'RomanH' --lim-mag 25.4 --param 'md' --paramvals '[0.001]' --title 'Roman/$\textit{H}$-band: 0.001 $M_{\odot}$ low-$Y_e$ mass'
python plot_contours.py --instr 'Roman' -f 'RomanH' --lim-mag 25.4 --param 'mw' --paramvals '[0.1]' --title 'Roman/$\textit{H}$-band: 0.1 $M_{\odot}$ high-$Y_e$ mass' --no-legend
python plot_contours.py --instr 'Roman' -f 'RomanH' --lim-mag 25.4 --param 'mw' --paramvals '[0.001]' --title 'Roman/$\textit{H}$-band: 0.001 $M_{\odot}$ high-$Y_e$ mass' --no-legend

python plot_contours.py --instr 'Roman' -f 'RomanH' --lim-mag 25.4 --param 'mw' 'md' --paramvals '[0.001]' '[0.001]' --title 'Roman/$\textit{H}$-band: 0.002 $M_{\odot}$ total ejecta mass'
python plot_contours.py --instr 'Roman' -f 'RomanH' --lim-mag 25.4 --param 'mw' 'md' --paramvals '[0.1]' '[0.1]' --title 'Roman/$\textit{H}$-band: 0.2 $M_{\odot}$ total ejecta mass' --no-legend



