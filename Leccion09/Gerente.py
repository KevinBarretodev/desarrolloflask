from Empleado import Empleado

class Gerente(Empleado):

    def __init__(self, nombre, sueldo, departamento):
        super().__init__(nombre, sueldo)
        self.departamento = departamento

    def __str__(self) -> str:
        return super().__str__() + f'[departamento : {self.departamento}]'