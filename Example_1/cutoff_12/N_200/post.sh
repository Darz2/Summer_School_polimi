#!/bin/bash

temp=("250")
press=("40e5" "60e5" "80e5" "100e5" "120e5" "140e5" "160e5" "180e5" "200e5")

outdir="TP"
if [ -d "$outdir" ]; then
    rm -rf "$outdir"
fi
mkdir -p "$outdir"

for t in "${temp[@]}"; do

    echo "Temperature[K] Pressure[Pascal] Density[kg/m3]" >> $outdir/density_"${t}".dat

    for p in "${press[@]}"; do
    
        echo "Temperature: $t, Pressure: $p"
        fold="T${t}_P${p}"
        
        cd "$fold/output" || exit

        density=$(grep 'Density average' -- ./*.txt | grep '\[kg.m' | awk '{print $3}')

        cd - || exit

        echo "$t $p $density" >> $outdir/density_"${t}".dat
    done

done