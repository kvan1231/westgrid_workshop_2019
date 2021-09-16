//============================================================================
#include <iostream>
#include <cmath>
#include <vector>

using namespace std;

//============================================================================
extern "C" {

//============================================================================
// Atomic clash finding function that uses output arrays preallocated
// on the Python side.
//============================================================================
int overlaps(const double* xx, const double* yy, const double* zz,
             const double* rr, int n,
             int max_nolaps, int* ii, int* jj, double* dd) {

	int nolaps = 0;

	// Iterate over a triangular matrix of atoms.
	for(int i = 0; i < n; i++) {
		for(int j = (i+1); j < n; j++) {

			double dx = xx[j] - xx[i];
			double dy = yy[j] - yy[i];
			double dz = zz[j] - zz[i];

			double rc = (rr[i] + rr[j]);
			
			double d2 = dx*dx + dy*dy + dz*dz;

			if(d2 < rc * rc) {
				// We have an overlap here.
				if(nolaps < max_nolaps) {
					ii[nolaps] = i;
					jj[nolaps] = j;
					dd[nolaps] = sqrt(d2);
				}
				nolaps++;
			}
		}
	}
	return nolaps;
}

//============================================================================
// A version with internal memory allocation.
//============================================================================
int overlaps_mem(const double* xx, const double* yy, const double* zz,
                 const double* rr, int n,
                 int** pii, int** pjj, double** pdd) {

	int nolaps = 0;

	vector<int> vii, vjj;
	vector<double> vdd;

	// Iterate over a triangular matrix of atoms.
	for(int i = 0; i < n; i++) {
		for(int j = (i + 1); j < n; j++) {

			double dx = xx[j] - xx[i];
			double dy = yy[j] - yy[i];
			double dz = zz[j] - zz[i];

			double rc = (rr[i] + rr[j]);
			
			double d2 = dx*dx + dy*dy + dz*dz;

			if(d2 < rc * rc) {
				// We have an overlap here.
				vii.push_back(i);
				vjj.push_back(j);
				vdd.push_back(sqrt(d2));
				nolaps++;
			}
		}
	}

	// Allocate memory here.
	int* ii = new int[nolaps];
	int* jj = new int[nolaps];
	double* dd = new double[nolaps];

	// Repackage the collected data into the output format.
	for(int k = 0; k < nolaps; k++) {
		ii[k] = vii[k];
		jj[k] = vjj[k];
		dd[k] = vdd[k];
	}

	// Copy the pointers to allocated memory to the output arrays.
	pii[0] = ii;
	pjj[0] = jj;
	pdd[0] = dd;

	return nolaps;
}

//============================================================================
// Function to free the allocated memory.
//============================================================================
void free_mem(int* ii, int* jj, double* dd) {
	
	delete[] ii;
	delete[] jj;
	delete[] dd;
}
//============================================================================
}	// End of extern "C" space
