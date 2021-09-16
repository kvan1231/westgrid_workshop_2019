#include <stdlib.h>
#include <stdio.h>
#include <netcdf.h>
#include <math.h>

#define FILE_NAME "stvol.nc"
#define nx 100

void handleError(int status) {
  if (status != NC_NOERR) {
    fprintf(stderr, "%s\n", nc_strerror(status));
    exit(-1);
  }
}

int main() {
  int ncid, x_dimid, y_dimid, z_dimid, varid, ny = nx, nz = nx, dimids[3], i, j, k;
  float x, y, z, (*data)[ny][nz];
  data = malloc(nx*sizeof *data);

  for (i = 0; i < nx; i++) {
    x = ((float)i+0.5)/(float)nx;
    x = 8.*(x-0.5);
    for (j = 0; j < ny; j++) {
      y = ((float)j+0.5)/(float)ny;
      y = 8.*(y-0.5);
      for (k = 0; k < nz; k++) {
	z = ((float)k+0.5)/(float)nz;
	z = 8.*(z-0.5);
	data[i][j][k] = 0.5*(pow(x,4)-16.*x*x+5.*x+pow(y,4)-16.*y*y+5.*y+pow(z,4)-16.*z*z+5.*z);
      }
    }
  }

  handleError(nc_create(FILE_NAME, NC_CLOBBER, &ncid));
  handleError(nc_def_dim(ncid, "z", nz, &z_dimid));
  handleError(nc_def_dim(ncid, "y", ny, &y_dimid));
  handleError(nc_def_dim(ncid, "x", nx, &x_dimid));

  dimids[0] = x_dimid;
  dimids[1] = y_dimid;
  dimids[2] = z_dimid;

  handleError(nc_def_var(ncid, "f(x,y,z)", NC_FLOAT, 3, dimids, &varid));
  handleError(nc_enddef(ncid));
  handleError(nc_put_var_float(ncid, varid, &data[0][0][0]));
  handleError(nc_close(ncid));

  free(data);
  return 0;
}
