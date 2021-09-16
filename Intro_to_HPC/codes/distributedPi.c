#include <stdio.h>
#include <math.h>
#include <mpi.h>
#define pi 3.14159265358979323846

int main(int argc, char *argv[])
{
  double total, h, sum, x;
  long long int i, n = 1e10;
  int rank, numprocs;

  MPI_Init(&argc, &argv);
  MPI_Comm_rank(MPI_COMM_WORLD, &rank);
  MPI_Comm_size(MPI_COMM_WORLD, &numprocs);

  h = 1./n;
  sum = 0.;

  if (rank == 0)
    printf("Calculating PI with %d processes\n", numprocs);

  printf("process %d started\n", rank);

  for (i = rank+1; i <= n; i += numprocs) {
    x = h * ( i - 0.5 );    //calculate at center of interval
    sum += 4.0 / ( 1.0 + pow(x,2));
  }

  sum *= h;
  MPI_Reduce(&sum,&total,1,MPI_DOUBLE,MPI_SUM,0,MPI_COMM_WORLD);

  if (rank == 0)
    printf("%.17g  %.17g\n", total, fabs(total-pi));

  MPI_Finalize();
  return 0;
}
