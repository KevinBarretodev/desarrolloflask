from Orden import Orden
from Producto import Producto


producto1 = Producto('Camisa', 78.00)
producto2 = Producto('Pantalon', 99.00)
productos1 = [producto1, producto2]

producto3 = Producto('T-SHIRT', 78.00)
producto4 = Producto('Pantalon CACQUI', 99.00)
productos2 = [producto3, producto4]

orden1 = Orden(productos1)
orden2 = Orden(productos2)

orden1.agregarProducto(producto3)
orden1.agregarProducto(producto4)
print(orden1)
print(orden1.calcularTotal())

# print(orden2)
# print(orden2.calcularTotal())
