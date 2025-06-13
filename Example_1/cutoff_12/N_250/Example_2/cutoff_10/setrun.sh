#!/bin/bash

src="src"


temp=("220" "230" "240" "250" "260" "270" "280")


for t in "${temp[@]}"; do
    echo "Temperature: $t"
    fold=$t

    mkdir -p "${fold}"

    cp ${src}/simulation.json      "${fold}"/.
    cp ${src}/submit.sh            "${fold}"/.
    cp ${src}/CO2.json             "${fold}"/.
    cp ${src}/force_field.json     "${fold}"/.
    cp ${src}/run.bat              "${fold}"/.
    cp ${src}/plot_file.py         "${fold}"/.
    cp ${src}/post_file.sh         "${fold}"/.

    sed -i "12s/TEMP/${t}/g"       "${fold}"/simulation.json  
    sed -i "22s/TEMP/${t}/g"       "${fold}"/simulation.json

    sed -i "2s/TEMP/${t}/g"       "${fold}"/submit.sh 

done


