#!/usr/bin/env python3

import pandas as pd, matplotlib.pyplot as plt

data = pd.read_csv("output_data.csv", delim_whitespace=True)

zero_indices = data.index[data['cycle'] == 0].tolist()
if len(zero_indices) >= 2:
    second_zero_index = zero_indices[1]
    prev_cycle_value = data.loc[second_zero_index - 1, 'cycle']
    
    offset = prev_cycle_value + 100
    data.loc[second_zero_index:, 'cycle'] += offset

# data.to_csv("modified_output_data.csv", sep=' ', index=False)
# print(data.head)

# Plot cycle vs density
plt.figure()
plt.plot(data["cycle"], data["density"], marker="o", linestyle="-")
plt.xlabel("Cycle")
plt.ylabel("Density / (kg/m³)")
plt.title("Cycle vs Density")
plt.grid(True)
plt.tight_layout()
plt.savefig("cycle_vs_density.png", dpi=300, bbox_inches="tight")
plt.close()

# Plot cycle vs energy
plt.figure()
plt.plot(data["cycle"], data["energy"], marker="o", linestyle="-")
plt.xlabel("Cycle")
plt.ylabel("Potential Energy / (K$_\mathrm{B}$)")
plt.title("Cycle vs Total Potential Energy")
plt.grid(True)
plt.tight_layout()
plt.savefig("cycle_vs_energy.png", dpi=300, bbox_inches="tight")
plt.close()

