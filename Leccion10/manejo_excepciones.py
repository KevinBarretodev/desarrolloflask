#Las excepciones todas heredan desde la clase BaseExxception o Exception, 
# estas clases de alta jerarquia pueden capturar cualquiera de las hijas

#En caso de capturar una excepcion se continua despues del try:except

#Esta herramienta puede tener multiples except en la misma estructura
#Se ingresa en Else cuando no se ejecuta ninguna excepcion
#El finally se va a ejecutar sea cual sea el error

from NumerosIdenticosException import NumerosIdenticosException

n =None
a= 10
b=10
try:

    if a == b:
        raise NumerosIdenticosException('Numeros identicos')
        
    n = a/b

except IndexError as e:

    print(f'Ha ocurrido un error {e}')

except TypeError as x:

    print(f'Algo ha salido mal, se ha capturado un TypeError {x}')

except Exception as ex:

    print(f'Ha ocurrido un error, capturando alta jerarquia {ex}')

else:
    print(f'No se ejecuto ninguna excepcion')

finally:
    print(f'Se ejecuta de todos modos sea cual sea el resultado')

print(f'Continuamos...')