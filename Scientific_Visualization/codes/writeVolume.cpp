#include <iostream>
#include <fstream>
#include <math.h>
using namespace std;

int main() {
  int i, j, k, n = 30;
  string filename = "cylinder.vtk";
  float x, y, z, f, r, r0 = 0.4;
  ofstream myfile;
  myfile.open(filename.c_str());
  myfile << "# vtk DataFile Version 3.0" << endl;
  myfile << "Volume example" << endl;
  myfile << "ASCII" << endl;
  myfile << "DATASET STRUCTURED_POINTS" << endl;
  myfile << "DIMENSIONS " << n << " " << n << " " << n << endl;
  myfile << "SPACING " << 1./(float)n << " " << 1./(float)n << " " << 1./(float)n << endl;
  myfile << "ORIGIN 0 0 0" << endl;
  myfile << "POINT_DATA " << n*n*n << endl;
  myfile << "SCALARS density float 1" << endl;
  myfile << "LOOKUP_TABLE default" << endl;
  for (i=0; i<n; i++) {
    x = ((float)i+0.5)/(float)n;
    for (j=0; j<n; j++) {
      y = ((float)j+0.5)/(float)n;
      for (k=0; k<n; k++) {
	z = ((float)k+0.5)/(float)n;
	r = sqrt((x-0.5)*(x-0.5)+(y-0.5)*(y-0.5));
	f = exp(-fabs(r-r0));
	myfile << f << endl;
      }}}
  myfile.close();
  return 0;
}
