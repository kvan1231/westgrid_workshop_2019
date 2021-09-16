import Image as im
a = im.open("fuji1.png")    # load image data from file
from pylab import *
nx = shape(a)[0]
ny = shape(a)[1]

c = a.load()
b_array = zeros((nx,ny),dtype=int)
for i in range(0,nx):
    for j in range(0,ny):
        b_array[i,j] = c[i,j][2]

gr = gradient(b_array)   # use only the blue band for edge detection
print shape(gr)
print shape(gr[0]), shape(gr[1])
gradientNormSquared = gr[0]**2 + gr[1]**2

for i in range(0,nx):
    for j in range(0,ny):
        value = int(gradientNormSquared[i,j])
        value = min(value,255)
        c[i,j] = (255-value,255-value,255-value)

a.show()    # display image
