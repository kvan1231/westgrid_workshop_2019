# codes/projectionFilter.py
input = self.GetInput(); output = self.GetOutput()
numPoints = input.GetNumberOfPoints(); numCells = input.GetNumberOfCells()
print numPoints, numCells
side = int(round(numPoints**(1./3.))); layer = side*side
pointData = input.GetPointData(); fref = pointData.GetArray('f(x,y,z)')
newPoints = vtk.vtkPoints()   # create 100x100 points forming the projection
proj = vtk.vtkDoubleArray()   # create the projection array
proj.SetName('projection')
for i in range(layer):
    x, y = input.GetPoint(i)[0:2]; z, pval = -30., 0.
    newPoints.InsertPoint(i,x,y,z)   # insert a point
    for j in range(side):
        pval += fref.GetValue(i+layer*j)
    proj.InsertNextValue(pval)   # add data to each point
output.SetPoints(newPoints); output.GetPointData().SetScalars(proj)
mesh = vtk.vtkCellArray()   # create 99x99 cells in the projection
for i in range(side-1):
    for j in range(side-1):
        mesh.InsertNextCell(4)   # insert a cell with four corners
        mesh.InsertCellPoint(i+j*side); mesh.InsertCellPoint(i+1+j*side)
        mesh.InsertCellPoint(i+side+j*side); mesh.InsertCellPoint(i+side+1+j*side)
output.SetCells(10, mesh)   # 10 refers to a VTK cell type
