#!/bin/bash
#SBATCH --time=00:15:00   # walltime in d-hh:mm or hh:mm:ss format
#SBATCH --job-name="rendering"
#SBATCH --mem=2000    # in MB
#SBATCH --account=def-razoumov-ws_cpu        # normally --account=your-ccdb-role
#SBATCH --reservation=arazoumov-may17        # normally no reservation
pvbatch --use-offscreen-rendering serialRendering.py
