#Clase estudiante



class Student:

    def __init__(self, nombre, apellido, correo, asignatura, codigoUM, celular):
        
        self._nombre = nombre
        self._apellido = apellido
        self._correo = correo
        self._asignatura = asignatura
        self._codigo = codigoUM
        self._celuar = celular

    def saludar(self):

        print(f'Hola, mi nombre es  {self._nombre}' )

    
    def setNombre(self, nombre):

        self._nombre = nombre

    
    def getNombre(self):

        return self._nombre

    def __del__(self):

        print(f'El objeto eliminado es {self._nombre}')

unit = Student("kevin", "barreto", "kbarreto@umanizales.com", "Fundamentos", 82201514991, "31242454322")

print(__name__)
print(unit.getNombre())
print("fiinalizar".center(50,'-'))
del unit

