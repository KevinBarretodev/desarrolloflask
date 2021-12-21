from Producto import Producto

class Orden:

    contador_ordenes = 0

    def __init__(self, productos) -> None:
        
        if isinstance(productos, list):

            Orden.contador_ordenes += 1
            self._id_orden = Orden.contador_ordenes
            self._productos = productos

        else:

            return 'No se ha creado ningun objeto porque no cumple parametros' 

    def agregarProducto(self, producto):

        if isinstance(producto, Producto):
            self._productos.append(producto)
        
        else:
            return 'No ha sido posible agregar este producto'

    def calcularTotal(self):

        total = 0

        for producto in self._productos:
            
            total += producto.getPrecio()
        
        return total

    def __str__(self) -> str:
        
        productos_srt = ''

        for producto in self._productos:

            productos_srt += producto.__str__() + '|'

        return f'Orden {self._id_orden} Productos {productos_srt}'





