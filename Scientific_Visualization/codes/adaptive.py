from pylab import *

def basicSimpson(f,a,b):
    quarter = 0.25*(b-a)
    x1 = a
    x2 = x1 + quarter
    x3 = x2 + quarter
    x4 = x3 + quarter
    x5 = b
    f1 = f(x1)
    f2 = f(x2)
    f3 = f(x3)
    f4 = f(x4)
    f5 = f(x5)
    s = (b-a)*(f1+4.*f3+f5)/6.
    error = 4./45. * (b-a) * abs(f1+f5-4.*(f2+f4)+6.*f3)
    return s, error

def partition(f,a,b,maxError):
    global k, x, integralArray, errorArray
    integral,error = basicSimpson(f,a,b)
    if abs(error) > maxError:
        midpoint = 0.5*(a+b)
        partition(f,a,midpoint,maxError)
        partition(f,midpoint,b,maxError)
    else:
        print 'interval =', a, b, ' --> ', integral, error
        x[k] = a
        integralArray[k] = integral
        errorArray[k] = error
        k += 1
    return

def simpsonAdaptive(f,a,b,maxError):
    global k, x, integralArray, errorArray
    k = 0
    x = zeros(1000)
    integralArray = zeros(1000)
    errorArray = zeros(1000)
    partition(f,a,b,maxError)
    x[k] = b
    print 'number of intervals =', k
    print 'total integral =', sum(integralArray[0:k+1])
    print 'total error <=', sum(errorArray[0:k+1])
    xmesh = x[0:k+1]
    ymesh = f(xmesh)
    plot(xmesh,ymesh,'ro')
    plot(xmesh,ymesh-ymesh,'kx')
    xx = linspace(a,b,1000)
    yy = f(xx)
    plot(xx,yy,'b-')
    grid(True)
    return
