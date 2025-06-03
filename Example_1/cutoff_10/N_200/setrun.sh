#!/bin/bash

src="src"
temp=("250")
press=("40e5" "60e5" "80e5" "100e5" "120e5" "140e5" "160e5" "180e5" "200e5")

for t in "${temp[@]}"; do
    for p in "${press[@]}"; do
    
        echo "Temperature: $t, Pressure: $p"
        fold="T${t}_P${p}"
        
        mkdir -p "${fold}"
        
        cp ${src}/simulation.json      "${fold}"/.
        cp ${src}/submit.sh            "${fold}"/.
        cp ${src}/CO2.json             "${fold}"/.
        cp ${src}/force_field.json     "${fold}"/.
        cp ${src}/run.bat              "${fold}"/.
        cp ${src}/plot_file.py         "${fold}"/.
        cp ${src}/post_file.sh         "${fold}"/.

        sed -i "12s/TEMP/${t}/g"       "${fold}"/simulation.json  
        sed -i "13s/PRESS/${p}/g"      "${fold}"/simulation.json

        sed -i "2s/TEMP/${t}/g"        "${fold}"/submit.sh
        sed -i "2s/PRESS/${p}/g"       "${fold}"/submit.sh 

    done

done


