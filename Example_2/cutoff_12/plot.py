#!/usr/bin/env python

############# Required Packages ############
import pandas as pd, numpy as np, matplotlib.pyplot as plt, PLOT_SETTINGS as ps
from matplotlib.ticker import MultipleLocator

############# Functions ############

def compute_relative_deviation(x_ref, y_ref, x_mc, y_mc):
    assert np.allclose(x_ref, x_mc)
    deviation = (y_mc - y_ref) / y_ref * 100
    return x_mc, deviation

############# Read files ############
NIST = pd.read_csv('NIST/CO2_VLE_NIST.dat', delimiter=' ').to_numpy()
MC   = pd.read_csv('TP/VLE_density.dat', delimiter=' ').to_numpy()
print(MC[:,0])


##################### PLOT #####################
fig, ax = ps.plot_init()

plt.plot(NIST[:,1], NIST[:,0], marker= 'o',
                markersize=ps.markersize,
                markerfacecolor=ps.face_colors[0],
                markeredgecolor='k',
                markeredgewidth=ps.markeredgewidth,
                linestyle='solid',
                linewidth= ps.linewidth,
                color=ps.colors[0],
                label=r'REFPROP',)

plt.plot(NIST[:,2], NIST[:,0], marker= 'o',
                markersize=ps.markersize,
                markerfacecolor=ps.face_colors[0],
                markeredgecolor='k',
                markeredgewidth=ps.markeredgewidth,
                linestyle='solid',
                linewidth= ps.linewidth,
                color=ps.colors[0])

plt.errorbar(MC[:, 1], MC[:, 0],
             xerr=MC[:, 2],
             fmt='o',
             markersize=ps.markersize,
             markerfacecolor=ps.face_colors[1],
             markeredgecolor='k',
             markeredgewidth=ps.markeredgewidth,
             linestyle='solid',
             linewidth=ps.linewidth,
             color=ps.colors[1],
             label=r'Monte Carlo')

plt.errorbar(MC[:, 3], MC[:, 0],
             xerr=MC[:, 4],
             fmt='o',
             markersize=ps.markersize,
             markerfacecolor=ps.face_colors[1],
             markeredgecolor='k',
             markeredgewidth=ps.markeredgewidth,
             linestyle='solid',
             linewidth=ps.linewidth,
             color=ps.colors[1])

plt.ylabel(rf"Temperature / [K]",fontsize=12)
plt.xlabel(rf"$\rho$ / [kg/m$^3$]",fontsize=12)
plt.legend(fontsize=8, loc= 'center')
# plt.xlim(0,33)
# plt.ylim(0,20)
# ax.yaxis.set_major_locator(MultipleLocator(10))
# ax.yaxis.set_minor_locator(MultipleLocator(5))
# ax.xaxis.set_major_locator(MultipleLocator(40))
# ax.xaxis.set_minor_locator(MultipleLocator(20))
   
ps.save_figure(fig, f"VLE_CO2.jpg")

plt.clf()

x_dev, dev = compute_relative_deviation(NIST[:,0], NIST[:,1], MC[:,0], MC[:,3])

plt.plot(x_dev, dev, marker='o',
         markersize=ps.markersize,
         markerfacecolor=ps.face_colors[-1],
         markeredgecolor='k',
         markeredgewidth=ps.markeredgewidth,
         linestyle='None',
         linewidth=ps.linewidth,
         color=ps.colors[-1],
         label=r'Relative Deviation')

plt.axhline(0, color='gray', linestyle='--', linewidth=1)
plt.xlabel(rf"Pressure / [bar]", fontsize=12)
plt.ylabel(r"Relative Deviation / [%]", fontsize=12)
# plt.xlim(0,33)
# plt.ylim(-2,2)
ps.save_figure(fig, "rel_dev_VLE.jpg")