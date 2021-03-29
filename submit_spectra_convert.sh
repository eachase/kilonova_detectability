#!/bin/bash
#SBATCH -A w20_knspectra
#SBATCH --time=00:05:00
#SBATCH --cpus-per-task=1
#SBATCH --nodes=1
#SBATCH --ntasks=5
#SBATCH --mem-per-cpu=600
#SBATCH -D /users/eachase/kilonovae/projects/kn_detectability/
#SBATCH -o log/submission.out
#SBATCH -e log/submission.err

submit_run="$(pwd)/run_convert.sh"

mkdir -p data/lightcurves/
cd data/lightcurves/

# For each redshift
for redshift in 0.0098 0.1 0.5 1.0 1.5
do
    # VRO (LSST)
    if (( $(echo "$redshift < 1.01" |bc -l) )); then
        mkdir -p VRO
        cd VRO
        mkdir -p "z_${redshift}"
        cd "z_${redshift}"
        echo "VRO ${redshift}"
        srun -N 1 -n 1 --export=REDSHIFT=${redshift},FILTERS="u-band" ${submit_run} >& log/out${i} &
        #export REDSHIFT=${redshift}
        #export FILTERS="r-band"
        #bash ${submit_run}
        cd ../../
    fi

    # Roman (WFIRST)
    mkdir -p Roman
    cd Roman
    echo "Roman ${redshift}"
    cd ../

    # Swift
    if (( $(echo "$redshift < 0.51" |bc -l) )); then
        mkdir -p Swift
        cd Swift
        echo "Swift ${redshift}"
        cd ../
    fi

    # SIBEX
    if (( $(echo "$redshift < 0.51" |bc -l) )); then
        mkdir -p SIBEX
        cd SIBEX
        echo "SIBEX ${redshift}"
        cd ../
    fi

    # ZTF

done













