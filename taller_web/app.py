from flask import Flask, render_template # importamos la libreria flask para poder construir la aplicacion.
import requests



app = Flask(__name__)
#Creamos la ruta
@app.route('/menu')
#Creamos una funcion que se va llamar menu
def menu():
    return render_template('menu.html')

@app.route("/personaje")
def personaje():
    api_URL = "https://rickandmortyapi.com/api/character/2"

    respuesta_api = requests.get(api_URL).json()

    nombre = respuesta_api["name"]
    estado = respuesta_api["status"]
    URL_imagen = respuesta_api["image"]
    
    return render_template('personaje.html', nombre_html = nombre, estado_html = estado, URL_imagen_html = URL_imagen)

if __name__ == '__main__':
    app.run(debug = True)


























