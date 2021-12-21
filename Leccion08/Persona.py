class Persona:

    def __init__(self, nombre, edad) -> None:
        self._nombre = nombre
        self._edad = edad

    def __add__(self, otro):
        return f'{self._nombre}  {otro._nombre}'

    def __sub__(self, otro):

        return self._edad - otro._edad


obj1 = Persona('Juan', 25)
obj2 = Persona('Carlos', 30)

print(obj1+obj2)
print(obj1-obj2)
