#!/bin/bash
#SBATCH --nodes=3        # number of nodes
#SBATCH --gres=gpu:1     # GPUs per node
#SBATCH --mem=4000M      # memory per node
#SBATCH --time=0-05:00   # walltime in d-hh:mm or hh:mm:ss format
#SBATCH --output=%N-%j.out   # %N for node name, %j for jobID
srun ./gpu_program
