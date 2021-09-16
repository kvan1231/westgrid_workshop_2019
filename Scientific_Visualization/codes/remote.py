from paraview.simple import *
sphere = Sphere()
print sphere.ThetaResolution
sphere.ThetaResolution = 16
Show()
WriteImage('image.png')
