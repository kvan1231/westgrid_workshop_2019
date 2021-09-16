/*=========================================================================
  Program:   Visualization Toolkit
  Module:    $RCSfile: vtkXMLHierarchicalBoxDataWriter.cxx,v $

  Copyright (c) Ken Martin, Will Schroeder, Bill Lorensen
  All rights reserved.
  See Copyright.txt or http://www.kitware.com/Copyright.htm for details.

  This software is distributed WITHOUT ANY WARRANTY; without even
  the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR
  PURPOSE.  See the above copyright notice for more information.
  =========================================================================*/

#include "vtkXMLHierarchicalBoxDataWriter.h"
#include "vtkAMRBox.h"
#include "vtkCompositeDataIterator.h"
#include "vtkHierarchicalBoxDataSet.h"
#include "vtkInformation.h"
#include "vtkMultiBlockDataSet.h"
#include "vtkObjectFactory.h"
#include "vtkSmartPointer.h"
#include "vtkXMLDataElement.h"
#include "vtkUniformGrid.h"

int main(int argc, char *argv[])
{

  vtkHierarchicalBoxDataSet *volume = vtkHierarchicalBoxDataSet::New();

  int numLevels = 2, nbase = 4;
  unsigned int numdatasets;
  volume->SetNumberOfLevels(numLevels);

  for (unsigned int level=0; level < numLevels; level++) {
    volume->SetRefinementRatio(level,2);
    // Set the number of datasets at this level
    if (level == 0) numdatasets = 1;
    if (level == 1) numdatasets = 3;
    volume->SetNumberOfDataSets(level, numdatasets);

    for (unsigned int dsindex=0; dsindex < numdatasets; dsindex++) {
      vtkAMRBox box;
      for (int j=0; j<3; j++) {
	box.LoCorner[j] = 0;
	box.HiCorner[j] = 4;
      }
      vtkUniformGrid *ug = vtkUniformGrid::New();
      ug->Initialize();

      if (level == 0) {
	ug->SetOrigin(0., 0., 0.);
	ug->SetDimensions(nbase, nbase, nbase);
      }

      if (level == 1) {
	if (dsindex == 0) ug->SetOrigin(0., 0., 0.);
	if (dsindex == 1) ug->SetOrigin(0.25, 0.25, 0.5);
	if (dsindex == 2) ug->SetOrigin(0., 0., 0.);
	ug->SetDimensions(4, 4, 4);
      }

      //      ug->GetDimensions(); // Call this so the dimensions array is set - stupid VTK

      float spacing = 1./(float(nbase)*pow(2.,level));
      ug->SetSpacing(spacing, spacing, spacing);
      ug->SetNumberOfScalarComponents(1);
      ug->SetScalarTypeToDouble();
      ug->AllocateScalars();

      // Set the dataset pointer for a given node
      volume->SetDataSet(level, dsindex, box, ug);

    }
  }

  // Write to file.
  vtkXMLHierarchicalBoxDataWriter *writer = vtkXMLHierarchicalBoxDataWriter::New();
  writer->SetInput(volume);
  writer->SetFileName("amr.vtm");
  writer->Write(); // the code breaks here

  return 0;
}
