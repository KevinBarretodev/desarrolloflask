# 'r' - Abre un archivo exclusivamente para la lectura, error si el archivo no existe
# 'a' - Abre un archivo para añadir informacion a la ya existente sin sobre escribir lo demas, crea el archivo si este no existe
# 'w' - Abre un archivo para la escritura, crea el archivo si no existe
# 'x' - Crea un archivo, devuelve error si ya existe

# Tambien se puede esecificar si el archivo que se va a manejar es binario o de texto


archivo = open('prueba.txt', 'r', encoding='utf-8') #Juego de caracteres que acepta acentos
# print(archivo.read())#Si se quiere leer solo una cantidad especifica de caracteres, se puede especificar denro del read(num)
# print(archivo.readline()) # Lee una linea a la vez

#El metodo readlines() devuelve una lista con todas las lineas
# for line in archivo:
#     print(archivo.readlines())

# print(archivo.readlines()[2])

archivo2 = open('copia.txt', 'a', encoding='utf-8')
archivo2.write(archivo.read())

archivo.close()
archivo2.close()