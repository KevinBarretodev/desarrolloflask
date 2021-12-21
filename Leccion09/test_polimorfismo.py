from Empleado import Empleado
from Gerente import Gerente

def imprimirDetalle(objeto):
    print(objeto)
    print(type(objeto))


empleado = Empleado('kevin', 3000000)

imprimirDetalle(empleado)

gerente = Gerente('kevin', 3000000, 'DataLab')

imprimirDetalle(gerente)