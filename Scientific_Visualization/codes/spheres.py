from paraview.simple import *

sineEnvelopenc = NetCDFReader(FileName=['/home/razoumov/data/sineEnvelope.nc'])
sineEnvelopenc.Dimensions = '(x, y, z)'

renderView1 = GetActiveViewOrCreate('RenderView')
renderView1.ViewSize = [900, 800]

sineEnvelopencDisplay = Show(sineEnvelopenc, renderView1)
sineEnvelopencDisplay.Representation = 'Outline'
sineEnvelopencDisplay.ColorArrayName = [None, '']
sineEnvelopencDisplay.OSPRayScaleArray = 'density'
sineEnvelopencDisplay.OSPRayScaleFunction = 'PiecewiseFunction'
sineEnvelopencDisplay.SelectOrientationVectors = 'None'
sineEnvelopencDisplay.ScaleFactor = 9.9
sineEnvelopencDisplay.SelectScaleArray = 'None'
sineEnvelopencDisplay.PolarAxes = 'PolarAxesRepresentation'
sineEnvelopencDisplay.ScalarOpacityUnitDistance = 1.7320508075688779
sineEnvelopencDisplay.Slice = 49
sineEnvelopencDisplay.SetRepresentationType('Surface')

renderView1.ResetCamera()

processIdScalars1 = ProcessIdScalars(Input=sineEnvelopenc)
processIdScalars1Display = Show(processIdScalars1, renderView1)
processIdScalars1Display.Representation = 'Outline'
processIdScalars1Display.ColorArrayName = ['POINTS', '']
processIdScalars1Display.OSPRayScaleArray = 'ProcessId'
processIdScalars1Display.OSPRayScaleFunction = 'PiecewiseFunction'
processIdScalars1Display.SelectOrientationVectors = 'None'
processIdScalars1Display.ScaleFactor = 9.9
processIdScalars1Display.SelectScaleArray = 'ProcessId'
processIdScalars1Display.PolarAxes = 'PolarAxesRepresentation'
processIdScalars1Display.ScalarOpacityUnitDistance = 1.7320508075688779
processIdScalars1Display.Slice = 49

Hide(sineEnvelopenc, renderView1)

processIdScalars1Display.SetRepresentationType('Surface')

ColorBy(processIdScalars1Display, ('POINTS', 'ProcessId'))

processIdScalars1Display.RescaleTransferFunctionToDataRange(True, False)

processIdScalars1Display.SetScalarBarVisibility(renderView1, True)

processIdLUT = GetColorTransferFunction('ProcessId')
processIdLUT.RGBPoints = [0.0, 0.231373, 0.298039, 0.752941, 1.5, 0.865003, 0.865003, 0.865003, 3.0, 0.705882, 0.0156863, 0.14902]
processIdLUT.ScalarRangeInitialized = 1.0

glyph1 = Glyph(Input=processIdScalars1, GlyphType='Sphere')
glyph1.GlyphTransform = 'Transform2'
glyph1.Scalars = ['POINTS', 'density']
glyph1.ScaleMode = 'scalar'
glyph1.ScaleFactor = 3.5

densityLUT = GetColorTransferFunction('density')
densityLUT.RGBPoints = [0.025424012914299965, 0.231373, 0.298039, 0.752941, 1.008953575976193, 0.865003, 0.865003, 0.865003, 1.992483139038086, 0.705882, 0.0156863, 0.14902]
densityLUT.ScalarRangeInitialized = 1.0

glyph1Display = Show(glyph1, renderView1)
glyph1Display.Representation = 'Surface'
glyph1Display.ColorArrayName = ['POINTS', 'density']
glyph1Display.LookupTable = densityLUT
glyph1Display.OSPRayScaleArray = 'density'
glyph1Display.OSPRayScaleFunction = 'PiecewiseFunction'
glyph1Display.SelectOrientationVectors = 'None'
glyph1Display.ScaleFactor = 10.53957076072693
glyph1Display.SelectScaleArray = 'density'
glyph1Display.GlyphType = 'Arrow'
glyph1Display.PolarAxes = 'PolarAxesRepresentation'
glyph1Display.GaussianRadius = 5.269785380363465
glyph1Display.SetScaleArray = ['POINTS', 'density']
glyph1Display.ScaleTransferFunction = 'PiecewiseFunction'
glyph1Display.OpacityArray = ['POINTS', 'density']
glyph1Display.OpacityTransferFunction = 'PiecewiseFunction'
glyph1Display.SetScalarBarVisibility(renderView1, True)

ColorBy(glyph1Display, ('POINTS', 'ProcessId'))

HideScalarBarIfNotNeeded(densityLUT, renderView1)

glyph1Display.RescaleTransferFunctionToDataRange(True, False)
glyph1Display.SetScalarBarVisibility(renderView1, True)

SetActiveSource(processIdScalars1)

processIdScalars1Display.Opacity = 0.4

renderView1.CameraPosition = [-207.0894359935346, 122.41918870990149, 246.04251060472586]
renderView1.CameraFocalPoint = [52.10105747288189, 45.362346749324146, 54.68937867674681]
renderView1.CameraViewUp = [0.15407693101374384, 0.9710860879216012, -0.1823516086424967]
renderView1.CameraParallelScale = 85.73651497465943
renderView1.OrientationAxesVisibility = 0

SaveScreenshot('/home/razoumov/data/regions.png', renderView1)
