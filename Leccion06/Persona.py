

class Persona:

    contador_personas = 0

    @classmethod
    def generarSigienteValor(cls):
        cls.contador_personas += 1
        return cls.contador_personas


        return
    
    def __init__(self, nombre, edad) -> None:
        Persona.generarSigienteValor()
        self.id_persona = Persona.contador_personas
        self.nombre = nombre
        self.edad = edad

    def __str__(self) -> str:
        return f'[Persona {self.id_persona} {self.nombre} {self.edad}]'


obj1 = Persona('kevin', 12)
obj2 = Persona('Daniela', 76)
obj3 = Persona('Charles', 25)
Persona.generarSigienteValor()
obj4 = Persona('Manuela', 28)

lista = [obj1, obj2, obj3]

for persona in lista:
    print(persona)
print(Persona.contador_personas)


    

    