#!/bin/bash
#SBATCH --gres=gpu:1       # GPUs per node
#SBATCH --mem=2000M        # memory per node
#SBATCH --time=0-05:00     # walltime in d-hh:mm or hh:mm:ss format
#SBATCH --account=your-ccdb-role
unset DISPLAY
pvbatch batch.py
