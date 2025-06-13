#!/bin/bash

temp=("220" "230" "240" "250" "260" "270" "280")

outdir="TP"
if [ -d "$outdir" ]; then
    rm -rf "$outdir"
fi
mkdir -p "$outdir"

echo "Temperature[K] Density-s0[kg/m3] SD-Density-s0[kg/m3] Density-s1[kg/m3] SD-Density-s1[kg/m3] Psat-s0[bar] SD-Psat-s0[bar]" >> $outdir/VLE_density.dat


for t in "${temp[@]}"; do
    
    echo "Temperature: $t"
    fold="${t}"
    
    cd "$fold/output" || exit

    density_s0=$(grep 'Density average' -- ./*s0.txt | grep '\[kg.m' | awk '{print $3}')
    SD_density_s0=$(grep 'Density average' -- ./*s0.txt | grep '\[kg.m' | awk '{print $5}')

    density_s1=$(grep 'Density average' -- ./*s1.txt | grep '\[kg.m' | awk '{print $3}')
    SD_density_s1=$(grep 'Density average' -- ./*s1.txt | grep '\[kg.m' | awk '{print $5}')

    Psat=$(awk '/Pressure average/ {getline; if ($0 ~ /\[bar\]/) print $(NF-3)}' ./*s0.txt)
    SD_Psat=$(awk '/Pressure average/ {getline; if ($0 ~ /\[bar\]/) print $(NF-1)}' ./*s0.txt)


    cd - || exit

    echo "$t $density_s0 $SD_density_s0 $density_s1 $SD_density_s1 $Psat $SD_Psat" >> $outdir/VLE_density.dat

done