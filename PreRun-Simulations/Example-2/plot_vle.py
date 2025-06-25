#!/usr/bin/env python

############# Required Packages ############
import pandas as pd, numpy as np, matplotlib.pyplot as plt

############# Read files ############
NIST = pd.read_csv('REFPROP/CO2_VLE_NIST.dat', delimiter=' ').to_numpy()

##################### VLE PLOT #####################
plt.figure()

plt.plot(NIST[:,1], NIST[:,0], marker='o',
         markersize=6,
         markerfacecolor='blue',
         markeredgecolor='k',
         markeredgewidth=1,
         linestyle='solid',
         linewidth=2,
         color='blue',
         label=r'REFPROP')

plt.plot(NIST[:,2], NIST[:,0], marker='o',
         markersize=6,
         markerfacecolor='blue',
         markeredgecolor='k',
         markeredgewidth=1,
         linestyle='solid',
         linewidth=2,
         color='blue')

plt.errorbar(41.33, 250,
             xerr=5.1,
             fmt='o',
             markersize=6,
             markerfacecolor='C1',
             markeredgecolor='k',
             markeredgewidth=1,
             linestyle='solid',
             linewidth=2,
             color='C1',
             label=r'Monte Carlo')

plt.errorbar(1039.61, 250,
             xerr=14.609,
             fmt='o',
             markersize=6,
             markerfacecolor='C1',
             markeredgecolor='k',
             markeredgewidth=1,
             linestyle='solid',
             linewidth=2,
             color='C1')

plt.ylabel(r"Temperature / [K]", fontsize=12)
plt.xlabel(r"$\rho$ / [kg/m$^3$]", fontsize=12)
plt.legend(fontsize=8, loc='best')
# plt.xlim(0,33)
# plt.ylim(0,20)
plt.tight_layout()
plt.savefig("VLE_CO2.jpg")

############# Saturation pressure plot ############

plt.clf()

plt.plot(NIST[:,0], NIST[:,3], marker='o',
         markersize=6,
         markerfacecolor='blue',
         markeredgecolor='k',
         markeredgewidth=1,
         linestyle='solid',
         linewidth=2,
         color='blue',
         label=r'REFPROP')

plt.errorbar(250,16.848,
             yerr=2.11,
             fmt='o',
             markersize=6,
             markerfacecolor='C1',
             markeredgecolor='k',
             markeredgewidth=1,
             linestyle='solid',
             linewidth=2,
             color='C1',
             label=r'Monte Carlo')

plt.xlabel(r"Temperature / [K]", fontsize=12)
plt.ylabel(r"Pressure / [bar]", fontsize=12)
plt.legend(fontsize=8, loc='best')
# plt.xlim(0,33)
# plt.ylim(0,20)
plt.tight_layout()
plt.savefig("VLE_CO2_Psat.jpg")