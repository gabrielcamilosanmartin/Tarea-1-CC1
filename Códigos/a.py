import numpy

def machineEpsilon(precision):
    if(precision=="simple"):
        funcion=numpy.float32
    else:
        funcion=numpy.float64
        
    e_mach = funcion(1)
    while funcion(1)+funcion(e_mach) != funcion(1):
        e_mach2 = e_mach
        e_mach = funcion(e_mach) / funcion(2)
    return e_mach2


print "epsilon machine single presicion: "+str(machineEpsilon("simple"))
print "epsilon machine doble presicion: "+str(machineEpsilon("double"))