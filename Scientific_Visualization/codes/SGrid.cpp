/*=========================================================================

  Program: modified from Visualization Toolkit example
  VTK/Examples/DataManipulation/Cxx/SGrid.cxx

=========================================================================*/

#include "vtkActor.h"
#include "vtkCamera.h"
#include "vtkFloatArray.h"
#include "vtkHedgeHog.h"
#include "vtkMath.h"
#include "vtkPointData.h"
#include "vtkPoints.h"
#include "vtkPolyDataMapper.h"
#include "vtkProperty.h"
#include "vtkRenderWindow.h"
#include "vtkRenderWindowInteractor.h"
#include "vtkRenderer.h"
#include "vtkStructuredGrid.h"
#include "vtkXMLStructuredGridWriter.h"

int main() {
  int i, j, k, kOffset, jOffset, offset;
  float x[3], a, v[3], rMin = 0.5, rMax = 1., deltaRad, deltaZ;
  float radius, theta;
  static int dims[3] = {13,11,11};

  // Create the structured grid.
  vtkStructuredGrid *sgrid = vtkStructuredGrid::New();
  sgrid->SetDimensions(dims);

  // Create points.
  vtkPoints *points = vtkPoints::New();
  points->Allocate(dims[0]*dims[1]*dims[2]);

  // Create scalars. No need to allocate size, as the array will expand automatically as we add new
  // values with InsertNextValue.
  vtkFloatArray *scalars = vtkFloatArray::New();
  scalars->SetName("density");

  // Create vectors.
  vtkFloatArray *vectors = vtkFloatArray::New();
  vectors->SetName("velocity");
  vectors->SetNumberOfComponents(3);
  vectors->SetNumberOfTuples(dims[0]*dims[1]*dims[2]);

  // Fill in the values for point coordinates and vectors one-by-one. Add points and vectors to the
  // structuted grid. The points form a hemi-cylinder of data.
  deltaZ = 2.0 / (dims[2]-1);
  deltaRad = (rMax-rMin) / (dims[1]-1);
  v[2] = 0.;
  for (k=0; k<dims[2]; k++) {
    x[2] = -1.0 + k*deltaZ;
    kOffset = k * dims[0] * dims[1];
    for (j=0; j<dims[1]; j++) {
      radius = rMin + j*deltaRad;
      jOffset = j * dims[0];
      for (i=0; i<dims[0]; i++) {
	theta = i * vtkMath::RadiansFromDegrees(15.0);
	x[0] = radius * cos(theta);
	x[1] = radius * sin(theta);
	v[0] = -x[1];
	v[1] = x[0];
	a = 1./radius;
	offset = i + jOffset + kOffset;
	points->InsertPoint(offset,x);
	vectors->InsertTuple(offset,v);
	scalars->InsertNextValue(a); // the array will expand automatically
      }
    }
  }
  sgrid->SetPoints(points);
  points->Delete();
  sgrid->GetPointData()->SetVectors(vectors);
  vectors->Delete();
  sgrid->GetPointData()->SetScalars(scalars);
  scalars->Delete();

  // Write to file.
  vtkXMLStructuredGridWriter *Writer = vtkXMLStructuredGridWriter::New();
  Writer->SetInputData(sgrid);
  Writer->SetFileName("halfCylinder.vts");
  Writer->Write();

  // Delete objects.
  Writer->Delete();
  sgrid->Delete();

  return 0;
}
