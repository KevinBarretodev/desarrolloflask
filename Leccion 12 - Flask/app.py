from flask import Flask, render_template, url_for
import requests
import json
from werkzeug.utils import redirect


app = Flask(__name__)

@app.route('/')
def hello():
    # Tambien hay logger.debug .warn .error y .info
    app.logger.info('Mensaje de nformacion')
    return f'Hello'


# De esta manera se envian parametros en la url, si se establece sera obligatorio el parametro.
@app.route('/saludar/<nombre>')
def saludar(nombre):

    # jsonData = json.request
    # El primer parametro es el template y el segundo las posibles llaves
    # render_template es una funcion que nos permite retornar una vista html en lugar de un 
    # objeto o texto y es una libreria implicita el Flask
    return render_template('mostrar.html', nombre_llave=nombre)
    # Se pueden pasar los parametros que sean necesarios

@app.route('/edad/<int:edad>', methods=['GET','POST'])
def mostrarEdad(edad):

    return f'Tu edad es : {edad}'


@app.route('/redireccionar')
def redirigir():
    # Se recomienda usar el url_for() en lugar de la ruta directa
    # Con redirect() nos permite redireccionar a una , el parametro que se le pasa
    # es la funcion de una de las rutas definidas o tambien cualquier direccion publica en internet
    return redirect(url_for('mostrarEdad', edad=20))
    # return redirect('https://martinfowler.com/articles/data-monolith-to-mesh.html')