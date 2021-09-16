from paraview.simple import *

path = '/Users/razoumov/Documents/workshops/visualization/data/' # edit the path accordingly
test_vts = XMLStructuredGridReader(FileName=[path+'halfCylinder.vts'])

DataRepresentation1 = Show() # turn on outline
DataRepresentation1.Representation = 'Outline'
DataRepresentation1.EdgeColor = [0.0, 0.0, 0.5]

# set camera position
RenderView = GetRenderView()
RenderView.CameraViewUp = [-0.25, 0.82, -0.51]
RenderView.CameraFocalPoint = [0., 0.5, 0.]
RenderView.CameraClippingRange = [2.91, 9.55]
RenderView.CameraPosition = [1.85, 3.79, 4.40]

Glyph2 = Glyph(GlyphType="Arrow" )
Glyph2.Scalars = ['POINTS', 'density']
Glyph2.SetScaleFactor = 0.2
Glyph2.Vectors = ['POINTS', 'velocity']
Glyph2.SetScaleFactor = 0.2

DataRepresentation2 = Show() # turn on vectors
DataRepresentation2.EdgeColor = [0.0, 0.0, 0.5]
DataRepresentation2.ColorAttributeType = 'POINT_DATA'
DataRepresentation2.ColorArrayName = 'density'

# set colour table
a1_density_PiecewiseFunction = CreatePiecewiseFunction( Points=[-15.70, 0.0, -5.7, 0.0, -4.23, 0.0, -4.07, 0.1, -3.21, 0.97, 0.0, 1.0] )
a1_density_PVLookupTable = GetLookupTableForArray( "density", 1, RGBPoints=[1.0, 0.0, 0.0, 0.0, 1.64, 0.90, 0.0, 0.0, 1.73, 0.90, 0.324, 0.0, 1.74, 0.90, 0.36, 0.0, 1.80, 0.90, 0.90, 0.0, 2.0, 1.0, 1.0, 1.0], VectorMode='Magnitude', ColorSpace='RGB', ScalarRangeInitialized=1.0 )
DataRepresentation2.LookupTable = a1_density_PVLookupTable

WriteImage('/Users/razoumov/Desktop/output.png')
Render()
