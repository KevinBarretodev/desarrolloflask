class Persona(object):

    def __init__(self, nombre, edad):
        self._nombre = nombre
        self._edad =edad
    
    def mostrarObjeto(self):
        return f'Hola mi nombre es {self._nombre} y mi edad es {self._edad}'

    def __str__(self) -> str:
        return f'Persona {self._nombre} De edad {self._edad}'

class Empleaddo (Persona):

    def __init__(self, nombre, edad, sueldo):
        super().__init__(nombre, edad)
        self._sueldo = sueldo

    def mostrarObjeto(self):
        return super().mostrarObjeto() + f'Mi sueldo es {self._sueldo}'

#Creacion objeto padre
persona1 = Persona('kevin', 'barreto')
print(persona1.mostrarObjeto())

#Creacion objeto hijo
persona2 = Empleaddo('juan', 'Shumaher', 5000000)
print(persona2.mostrarObjeto())

print(persona1)
