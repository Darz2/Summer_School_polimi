#!/usr/bin/env python

"""
REFPROP.py
Created by Darshan on 2024-06-11.
This script provides functionality related to thermophysical property calculations,
utilizing the REFPROP library for fluid properties.

Created by Darshan.
"""

import os, sys, re, subprocess
import numpy as np, CoolProp.CoolProp as CP

refprop_path = os.path.expanduser('~/Software/REFPROP/REFPROP-cmake/build')
CP.set_config_string(CP.ALTERNATIVE_REFPROP_PATH, refprop_path)

############################### TEST #################################
# print("The speed of sound calulated in REFPROP using GERG 2008 EOS:  " + str(CP.PropsSI("A","T",313,"P",200e5,"REFPROP::Nitrogen")))

########### MODIFICATION SPACE ###################
pressure = np.arange(40, 201, 10)
pressure = [x*1e5 for x in pressure]
temperature = np.array([250])

bash_code = '''
if [ -d "NIST" ]; then
    rm -r "NIST"
fi
mkdir "NIST"
'''

subprocess.call(bash_code, shell=True)

for T in temperature:
    for P in pressure:
        
        density_kg = CP.PropsSI("D","T",T,"P",P,"REFPROP::CO2")
        file_properties = os.path.join(os.getcwd(), f"NIST/TP_{T}_NIST.dat")
        
        if not os.path.isfile(file_properties):
            with open(file_properties, "w") as file:
                file.write("Temperature[K] Pressure[bar] Density[kg/m3]\n")
                file.write(f"{T:.1f} {P/1e5:.1f} {density_kg:.4f}\n")

        else:
            with open(file_properties, "a") as file:
                file.write(f"{T:.1f} {P/1e5:.1f} {density_kg:.4f}\n")
                
#END