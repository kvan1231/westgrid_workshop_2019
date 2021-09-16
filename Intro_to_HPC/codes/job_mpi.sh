#!/bin/bash
#SBATCH --ntasks=4        # number of MPI processes
#SBATCH --time=0-00:05    # walltime in d-hh:mm or hh:mm:ss format
#SBATCH --mem-per-cpu=100 # in MB
mpirun -np $SLURM_NTASKS ./mpi                # or `srun ./mpi`
