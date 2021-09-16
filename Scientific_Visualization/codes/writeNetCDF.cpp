#include <iostream>
#include <netcdf>
#include <fstream>
#include <math.h>
using namespace std;
using namespace netCDF;
using namespace netCDF::exceptions;

/* this program writes data in NetCDF */

#define nx 100
#define ny nx
#define nz nx
#define NC_ERR 2

float data[nx][ny][nz]; // neeed contiguous storage for NetCDF, so no dynamic allocation; allocate in global heap

int main() {
  int ncid, x_dimid, y_dimid, z_dimid;
  int dimids[3], retval, i, j, k;
  float x, y, z, r, r0 = 0.4;

  for (i = 0; i < nx; i++) {
    if (nx > 100 && i%100 == 0) cout << i << endl;
    x = ((float)i+0.5)/(float)nx;
    for (j = 0; j < ny; j++) {
      y = ((float)j+0.5)/(float)ny;
      for (k = 0; k < nz; k++) {
	z = ((float)k+0.5)/(float)nz;
	r = sqrt(pow(x-0.5,2)+pow(y-0.5,2));
	data[i][j][k] = exp(-sqrt(pow(z-0.5,2)+pow(r-r0,2)));
      }
    }
  }

  try {
    NcFile fileHandle("volume.nc", NcFile::replace);
    NcDim xDim = fileHandle.addDim("x", nx);
    NcDim yDim = fileHandle.addDim("y", ny);
    NcDim zDim = fileHandle.addDim("z", nz);
    vector<NcDim> dims;
    dims.push_back(xDim);
    dims.push_back(yDim);
    dims.push_back(zDim);
    NcVar varID = fileHandle.addVar("density", ncFloat, dims);
    varID.putVar(data);
    return 0;
  }
  catch(NcException& e) {
    e.what();
    return NC_ERR;
  }
}
