#!/usr/bin/env python3

import pandas as pd, matplotlib.pyplot as plt

files = [("output_data_s0.csv", "s0"), ("output_data_s1.csv", "s1")]

for filename, suffix in files:
    data = pd.read_csv(filename, delim_whitespace=True)

    # Adjust cycle if two or more zeros are found
    zero_indices = data.index[data['cycle'] == 0].tolist()
    if len(zero_indices) >= 2:
        second_zero_index = zero_indices[1]
        prev_cycle_value = data.loc[second_zero_index - 1, 'cycle']
        offset = prev_cycle_value + 100
        data.loc[second_zero_index:, 'cycle'] += offset

    # Plot cycle vs density
    plt.figure()
    plt.plot(data["cycle"], data["density"], marker="o", linestyle="-")
    plt.xlabel("Cycle")
    plt.ylabel("Density / (kg/m³)")
    plt.title(f"Cycle vs Density ({suffix})")
    plt.grid(True)
    plt.tight_layout()
    plt.savefig(f"cycle_vs_density_{suffix}.png", dpi=300, bbox_inches="tight")
    plt.close()

    # Plot cycle vs energy
    plt.figure()
    plt.plot(data["cycle"], data["energy"], marker="o", linestyle="-")
    plt.xlabel("Cycle")
    plt.ylabel("Potential Energy / (K$_\\mathrm{B}$)")
    plt.title(f"Cycle vs Total Potential Energy ({suffix})")
    plt.grid(True)
    plt.tight_layout()
    plt.savefig(f"cycle_vs_energy_{suffix}.png", dpi=300, bbox_inches="tight")
    plt.close()