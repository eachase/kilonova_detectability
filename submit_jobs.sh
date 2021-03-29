#!/bin/bash
#SBATCH -A w20_knspectra
#SBATCH --time=05:00:00
#SBATCH --array=1-42%36
#SBATCH --ntasks-per-node=36
#SBATCH --mem-per-cpu=600
#SBATCH -D /users/eachase/kilonovae/projects/kn_detectability/
#SBATCH -o log/job_%A_%a.out
#SBATCH -e log/job_%A_%a.err

MY_MACHINE=grizzly
mkdir -p log

echo "======================= start =========================="
date

set -- $(sed -n ${SLURM_ARRAY_TASK_ID}p input_jobs.csv | sed 's/,/ /g')

redshift=$1
filters=$2
echo python -u convert_lightcurves --redshift "$redshift" -f "$filters"
python -u convert_lightcurves --redshift "$redshift" -f "$filters"

echo "======================== end ==========================="
date
