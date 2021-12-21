# La claúsula with no tiene en python la función de delimitar el espacio de nombres ("namespaces") 
# como se hace en otros lenguajes como VB. 
# Es más para determinar la configuración local que tendrá un bloque de código, lo que se conoce como "contexto".

# with open('prueba.txt', 'r', encoding='utf-8') as archivo:
#     print(archivo.read())

from ManejoArchivos import ManejoArchivos

with ManejoArchivos('prueba.txt') as archivo:
    print(archivo.read())

# Para controlar un contexto, se usan los "gestores de contexto" ("context manager") que son objetos que tienen 
# definidos los métodos __enter__ y __exit__. El primero para inicializar el contexto, el segundo para finalizarlo.

