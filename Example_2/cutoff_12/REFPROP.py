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
temperature = np.arange(220, 281, 5)

bash_code = '''
if [ -d "NIST" ]; then
    rm -r "NIST"
fi
mkdir "NIST"
'''

subprocess.call(bash_code, shell=True)

for T in temperature:
        
    density_liq      = CP.PropsSI("D","T",T,"Q",0,"REFPROP::CO2")
    density_vap      = CP.PropsSI("D","T",T,"Q",1,"REFPROP::CO2")
    Psat             = CP.PropsSI("P", "T", T, "Q", 0, "REFPROP::CO2")
    
    file_properties = os.path.join(os.getcwd(), f"NIST/CO2_VLE_NIST.dat")
    
    if not os.path.isfile(file_properties):
        with open(file_properties, "w") as file:
            file.write("Temperature[K] Density_liq[kg/m3] Density_vap[kg/m3] Saturation-Pressure(bar)\n")
            file.write(f"{T:.1f} {density_liq:.4f} {density_vap:.4f} {Psat/1e5:.4f}\n")
    else:
        with open(file_properties, "a") as file:
            file.write(f"{T:.1f} {density_liq:.4f} {density_vap:.4f} {Psat/1e5:.4f}\n")
                
#END