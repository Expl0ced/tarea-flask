import json
from flask import Flask, render_template
import random
app = Flask(__name__)
app.config.update(
    DEBUG=True,
    ENV='development'
)

def cargar_datos():
    ruta='pokedex.json'
    with open(ruta) as contenido:
        resultado=json.load(contenido)
        for i in range(1,151):
            pokemon=resultado['pokemon'][i]['name']
    return pokemon
name_poke=cargar_datos()
@app.route("/")
def index():
    return render_template("index.html", name_poke=cargar_datos())
