class Color:
    
    def __init__(self, color):
        self.color = color

    def setColor(self, color):
        self.color = color

    def getColor(self):
        return self.color

    def __str__(self) -> str:
        return f'Objeto Color {self.color}'


