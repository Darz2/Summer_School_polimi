#!/bin/bash
#SBATCH -J 220
#SBATCH -n 1
#SBATCH -p serial-short
#SBATCH -t 06:00:00
#SBATCH --mail-type=FAIL
#SBATCH --mail-user=d.raju@tudelft.nl

echo "Job started at $(date)"

START_TIME=$(date +%s)

raspa3 simulation.json

END_TIME=$(date +%s)
ELAPSED_TIME=$((END_TIME - START_TIME))
ELAPSED_MINUTES=$(echo "scale=2; $ELAPSED_TIME / 60" | bc)

echo "Job ended at $(date)"

echo "Elapsed time: $ELAPSED_MINUTES minutes"