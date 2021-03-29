#!/bin/bash

MY_MACHINE=grizzly

echo "======================= start =========================="
date

cd ../../../../
convert_lightcurves="$(pwd)/convert_lightcurves"

echo python -u ${convert_lightcurves} --redshift "$REDSHIFT" -f "$FILTERS"
#python -u ${convert_lightcurves} --redshift "$REDSHIFT" -f "$FILTERS"


echo "======================== end ==========================="
date




