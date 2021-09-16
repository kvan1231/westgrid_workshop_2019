from paraview.simple import *

path = '/Users/razoumov/Documents/workshops/visualization/data/'
reader = OpenDataFile(path+'halfCylinder.vts')  # edit the file location

Show()
Render()

print 'print all variables'
print reader.PointData[:]

print 'get a handle to PointData and print all point fields'
pd = reader.PointData
print pd.keys()

print 'get some info about individual fields'
print pd['density'].GetNumberOfComponents()
print pd['density'].GetRange()
print pd['velocity'].GetNumberOfComponents()

print 'run through all arrays and print the ranges of all components'
for ai in pd.values():
    print ai.GetName(), ai.GetNumberOfComponents()
    for i in xrange(ai.GetNumberOfComponents()):
        print i, ai.GetRange(i)
