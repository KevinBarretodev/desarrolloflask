from _typeshed import SupportsReadline
from FiguraGeometrica import FiguraGeometrica
from Color import Color

class Cuadrado(FiguraGeometrica, Color):

    def __init__(self, alto, color):
        
        FiguraGeometrica.__init__(self,alto, alto)
        Color.__init__(self, color)


    def calcularArea(self):
        return self.alto * self.ancho

    def __str__(self):
        return f'Objeto tipo cuadrado con alto {self.alto}, ancho {self.ancho} y color {self.color}'


    


