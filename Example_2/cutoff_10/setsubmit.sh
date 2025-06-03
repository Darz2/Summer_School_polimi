#!/bin/bash


temp=("220" "230" "240" "250" "260" "270" "280")


for t in "${temp[@]}"; do

    fold=$t
    
    cd "$fold" || exit
    sbatch submit.sh

    cd - || exit

done