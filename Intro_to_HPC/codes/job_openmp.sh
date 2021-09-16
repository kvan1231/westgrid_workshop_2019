#!/bin/bash
#SBATCH --cpus-per-task=2   # number of cores
#SBATCH --time=0-00:05      # walltime in d-hh:mm or hh:mm:ss format
#SBATCH --mem=100           # 100M for the whole job (all threads)
export OMP_NUM_THREADS=$SLURM_CPUS_PER_TASK   # passed to the program
echo running on $SLURM_CPUS_PER_TASK cores
./openmp
