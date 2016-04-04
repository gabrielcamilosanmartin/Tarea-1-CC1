import numpy

def distancia_double(x,y,z):
    aux=numpy.float64(0)
    return ((x-aux)*(x-aux)+(y-aux)*(y-aux)+(z-aux)*(z-aux))**(0.5)
def distancia_simple(x,y,z):
    aux=numpy.float32(0)
    return ((x-aux)*(x-aux)+(y-aux)*(y-aux)+(z-aux)*(z-aux))**(0.5)

funcion64=numpy.float64
funcion32=numpy.float32
print "distancia precision simple: "+str(distancia_double(funcion32(9.4**5),funcion32(0.7**5),funcion32(7**5)))+"  distancia precision doble: "+str(distancia_double(funcion64(9.4**5),funcion64(0.7**5),funcion64(7**5)))
print "distancia precision simple: "+str(distancia_double(funcion32(0.2**5),funcion32(9.5**5),funcion32(6.1**5)))+"  distancia precision doble: "+str(distancia_double(funcion64(0.2**5),funcion64(9.5**5),funcion64(6.1**5)))
print "distancia precision simple: "+str(distancia_double(funcion32(0.6**5),funcion32(3.1**5),funcion32(2.5**5)))+"  distancia precision doble: "+str(distancia_double(funcion64(0.6**5),funcion64(3.1**5),funcion64(2.5**5)))
print "distancia precision simple: "+str(distancia_double(funcion32(9**5),funcion32(3.5**5),funcion32(4**5)))+"  distancia precision doble: "+str(distancia_double(funcion64(9**5),funcion64(3.5**5),funcion64(4**5)))