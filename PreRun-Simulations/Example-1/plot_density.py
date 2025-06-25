#!/usr/bin/env python

############# Required Packages ############
import pandas as pd, numpy as np, matplotlib.pyplot as plt

############# Read files ############
NIST = pd.read_csv('REFPROP/TP_250_NIST.dat', delimiter=' ').to_numpy()

##################### PLOT #####################
plt.figure()

plt.plot(NIST[:,1], NIST[:,2], marker='o',
         markersize=6,
         markerfacecolor='blue',
         markeredgecolor='k',
         markeredgewidth=1,
         linestyle='solid',
         linewidth=2,
         color='blue',
         label=r'REFPROP')

plt.errorbar(100, 1072.7,
             yerr=10,
             fmt='o',
             markersize=6,
             markerfacecolor='red',
             markeredgecolor='k',
             markeredgewidth=1,
             linestyle='solid',
             linewidth=2,
             color='red',
             label=r'Monte Carlo')

plt.xlabel(rf"Pressure / [bar]",fontsize=12)
plt.ylabel(rf"$\rho$ / [kg/m$^3$]",fontsize=12)
plt.legend(fontsize=8)
# plt.xlim(0,33)
# plt.ylim(0,20)
plt.tight_layout()
plt.savefig("Density.jpg")