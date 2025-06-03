#!/bin/bash


temp=("250")
press=("40e5" "60e5" "80e5" "100e5" "120e5" "140e5" "160e5" "180e5" "200e5")

for t in "${temp[@]}"; do
    for p in "${press[@]}"; do

        fold="T${t}_P${p}"
        
        cd "$fold" || exit
        sbatch submit.sh

        cd - || exit
        
    done
done