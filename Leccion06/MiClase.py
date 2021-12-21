class MiClase(object):


    variable_clase = 'Esta es mi variable de clase'

    def __init__(self, attr):
        self.attr = attr

    #Para este ipo de metodos se debe establecer con el decorador @staticmethod
    @staticmethod
    def funcionEstatica():
        return MiClase.variable_clase

    @classmethod
    def funcionDeClase(cls):
        return cls.variable_clase

print(MiClase.funcionDeClase())

# clase1 = MiClase('ejemplo instancia')
# print(clase1.attr)
# print(clase1.variable_clase)

print(MiClase.funcionEstatica())
