from math import pi
from mpi4py import MPI
import numpy as np
comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

n = 1000000
h = 1./n
sum = 0.

# if rank == 0:
#     print 'Calculating PI with', size, 'processes'

# print 'process', rank, 'of', size, 'started'

for i in range(rank, n, size):
    # print rank, i
    x = h * ( i + 0.5 )
    sum += 4. / ( 1. + x**2)

local = np.zeros(1)
total = np.zeros(1)
local[0] = sum*h
comm.Reduce(local, total, op = MPI.SUM)
if rank == 0:
    print total[0], abs(total[0]-pi)
