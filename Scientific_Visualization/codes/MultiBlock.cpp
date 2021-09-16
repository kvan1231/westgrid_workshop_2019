/*=========================================================================

  Program:   Visualization Toolkit
  Module:    $RCSfile: MultiBlock.cxx,v $

  Copyright (c) Ken Martin, Will Schroeder, Bill Lorensen
  All rights reserved.
  See Copyright.txt or http://www.kitware.com/Copyright.htm for details.

  This software is distributed WITHOUT ANY WARRANTY; without even
  the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR
  PURPOSE.  See the above copyright notice for more information.

  =========================================================================*/
// This example demonstrates how multi-block datasets can be processed
// using the new vtkMultiBlockDataSet class.
// 
// The command line arguments are:
// -D <path> => path to the data (VTKData); the data should be in <path>/Data/

#include "vtkActor.h"
#include "vtkCellDataToPointData.h"
#include "vtkCompositeDataGeometryFilter.h"
#include "vtkCompositeDataPipeline.h"
#include "vtkContourFilter.h"
#include "vtkDebugLeaks.h"
#include "vtkMultiBlockDataSet.h"
#include "vtkOutlineCornerFilter.h"
#include "vtkPolyData.h"
#include "vtkPolyDataMapper.h"
#include "vtkProperty.h"
#include "vtkRenderer.h"
#include "vtkRenderWindow.h"
#include "vtkRenderWindowInteractor.h"
#include "vtkShrinkPolyData.h"
#include "vtkStructuredGrid.h"
#include "vtkStructuredGridOutlineFilter.h"
#include "vtkTestUtilities.h"
#include "vtkXMLStructuredGridReader.h"
#include <vtksys/ios/sstream>
#include "vtkXMLMultiBlockDataWriter.h"
#include <string>
using namespace std;

int main(int argc, char *argv[])
{
  vtkCompositeDataPipeline *exec = vtkCompositeDataPipeline::New();
  vtkAlgorithm::SetDefaultExecutivePrototype(exec);
  exec->Delete();

  // Standard rendering classes
  vtkRenderer *ren = vtkRenderer::New();
  vtkRenderWindow *renWin = vtkRenderWindow::New();
  renWin->AddRenderer(ren);
  vtkRenderWindowInteractor *iren = vtkRenderWindowInteractor::New();
  iren->SetRenderWindow(renWin);

  // We will read three files and collect them together in one multi-block dataset.
  int i;
  vtkXMLStructuredGridReader *reader = vtkXMLStructuredGridReader::New();

  // vtkMultiBlockDataSet respresents multi-block datasets
  vtkMultiBlockDataSet *mb = vtkMultiBlockDataSet::New();

  char filename[90];

  for (i=0; i<3; i++) {
    // load three separate files (each containing a structured grid dataset)
    sprintf(filename, "%s%d%s", "../data/vtk/xml/multicomb_", i, ".vts");
    printf("%s\n", filename);
    reader->SetFileName(filename);
    // We have to update since we are working without a VTK pipeline.
    // This will read the file and the output of the reader will be
    // a valid structured grid data.
    reader->Update();
    // We create a copy to avoid adding the same data three
    // times (the output object of the reader does not change
    // when the filename changes)
    vtkStructuredGrid *sg = vtkStructuredGrid::New();
    sg->ShallowCopy(reader->GetOutput());
    // Add the structured grid to the multi-block dataset
    mb->SetBlock(i, sg);
    sg->Delete();
  }
  reader->Delete();

  // Write to file.
  vtkXMLMultiBlockDataWriter *Writer = vtkXMLMultiBlockDataWriter::New();
  Writer->SetInput(mb);
  Writer->SetFileName("multiblock.vtm");
  Writer->Write();

  // Delete objects.
  Writer->Delete();
  mb->Delete();

  return 0;
}
