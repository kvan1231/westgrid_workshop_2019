# codes/extractValues.py
from paraview.simple import *

dir = '/Users/razoumov/teaching/paraviewWorkshop/data/'
data = NetCDFReader(FileName=[dir+'stvol.nc'])
local = servermanager.Fetch(data) # get the data from the server
print local.GetNumberOfPoints()

for i in range(10):
    print local.GetPoint(i) # print coordinates of first 10 points

pd = local.GetPointData()
print pd.GetArrayName(0) # print the name of the first array

result = pd.GetArray('f(x,y,z)')
print result.GetDataSize()
print result.GetRange()

for i in range(10):
    print result.GetValue(i) # print values at first 10 points
