from paraview.simple import *

test_vts = XMLStructuredGridReader(FileName=['/Users/razoumov/Documents/workshops/visualization/data/halfCylinder.vts'])

# --- 1st method
DataRepresentation = Show()
DataRepresentation.Representation = 'Surface'
DataRepresentation.DiffuseColor = [0, 0, 1]
DataRepresentation.SpecularColor = [1, 1, 1]
DataRepresentation.SpecularPower = 200
DataRepresentation.Specular = 1

# --- 2nd method
# Show()
# handle = GetRepresentation()
# handle.Representation = 'Surface'
# handle.DiffuseColor = [0, 0, 1]
# handle.SpecularColor = [1, 1, 1]
# handle.SpecularPower = 200
# handle.Specular = 1

Render()
