#include <stdio.h>
#include <math.h>
#define pi 3.14159265358979323846

int main(int argc, char *argv[])
{
  double h, sum, x;
  long long int i, n = 1e10;
  h = 1./n;
  sum = 0.;

  for (i = 1; i <= n; i++) {
    x = h * ( i - 0.5 );
    sum += 4. / ( 1. + pow(x,2));
  }

  sum *= h;
  printf("%.17g  %.17g\n", sum, fabs(sum-pi));

  return 0;
}
