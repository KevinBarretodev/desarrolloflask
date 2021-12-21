#ABC = Abstract Base Class, es la que nos permite realizar la abstraccion de las clases

from abc import ABC, abstractmethod

class FiguraGeometrica(ABC):

    def __init__(self, ancho, alto):
        
        if self._validar_valor(ancho):
            self.ancho = ancho
        else:
            print(f'Valor incorrecto')


        if self._validar_valor(alto):
            self.alto = alto
        else:
            print(f'Valor incorrecto')

    def getAncho(self):
        return self.ancho

    def setAncho(self, ancho):
        self.ancho = ancho

    def getAlto(self):
        return self.alto

    def setAlto(self, alto):
        self.alto = alto

    @abstractmethod
    def calcularArea(self):
        pass

    def __str__(self):
        return f'Figura con alto {self.alto} y con ancho {self.ancho}'

    def _validar_valor(self, valor):
        return True if 0 < valor < 10 else False






