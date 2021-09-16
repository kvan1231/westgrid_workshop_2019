#!/bin/bash
#SBATCH --ntasks=4   # number of MPI processes
#SBATCH --time=0-00:05   # walltime in d-hh:mm or hh:mm:ss format
#SBATCH --job-name="rendering"
#SBATCH --mem-per-cpu=2000   # in MB
#SBATCH --account=def-razoumov-ws_cpu        # normally --account=your-ccdb-role
#SBATCH --reservation=arazoumov-may17        # normally no reservation
srun pvbatch --use-offscreen-rendering parallelRendering.py
