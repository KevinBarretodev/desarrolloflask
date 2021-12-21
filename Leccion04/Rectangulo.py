from FiguraGeometrica import FiguraGeometrica
from Color import Color

#Ejemplo de herencia multiple, es decir, ereda componentes de dos o mas clases
class Rectangulo(FiguraGeometrica, Color):

    def __init__(self, ancho, alto, color):
        FiguraGeometrica.__init__(self,ancho, alto)
        Color.__init__(self, color)

    def calcularArea(self):
        return self.ancho * self.alto

    def __str__(self):
        return f'Objeto tipo cuadrado con alto {self.alto}, ancho {self.ancho} y color {self.color}'