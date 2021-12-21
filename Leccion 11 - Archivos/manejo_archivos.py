try:
    #Con la funcion open() podemos realizar dos funciones, abrir un archivo existente o crear uno. Si no se especifica la ruta
    #se creara en la misma carpeta donde esta el ejecutable de Python
    archivo = open('prueba.txt', 'w', encoding='utf-8')
    archivo.write('Añadiento texto de prueba para verificar escritura')
except Exception as ex:
    print(ex)
finally:
    #Luego de que se cierra el archivo no se podra leer o escribir el archivo en la instancia actual.
    archivo.close()
