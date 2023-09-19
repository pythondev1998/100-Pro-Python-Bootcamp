from flask import Flask, render_template, request, jsonify
from flask_bootstrap import Bootstrap
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)
bootstrap = Bootstrap(app)

API_KEY = '6fe10dc10bbb40f5a620cb732a7b7072'

#SEARCH BAR
@app.route('/sugerencias', methods=['GET'])
def obtener_sugerencias():
    query = request.args.get('query')
    sugerencias = obtener_sugerencias_desde_api(query)  # Obtén las sugerencias según la consulta
    return jsonify(sugerencias)

# Función para obtener sugerencias desde la API de Spoonacular
def obtener_sugerencias_desde_api(query):
    url = f'https://api.spoonacular.com/recipes/complexSearch?query={query}&apiKey={API_KEY}&instructionsRequired=true&addRecipeNutrition=true'
    response = requests.get(url)
    data = response.json()
    sugerencias = []

    if 'results' in data and len(data['results']) > 0:
        for resultado in data['results']:
            titulo = resultado['title']
            sugerencias.append(titulo)

    return sugerencias
#######################



@app.route('/')
def index():
    return render_template('index.html')


@app.route('/buscar', methods=['GET'])
def buscar_platillo():
    platillo = request.args.get('platillo')
    info_platillo = obtener_info_platillo(platillo)  # Llama a la función para obtener información del platillo
    print(info_platillo)
    return render_template('index.html', platillo=platillo, **info_platillo)


def obtener_info_platillo(platillo):
    url = f'https://api.spoonacular.com/recipes/complexSearch?query={platillo}&apiKey={API_KEY}&instructionsRequired=true&addRecipeNutrition=true'

    try:
        response = requests.get(url)
        data = response.json()

        if 'results' in data and len(data['results']) > 0:
            resultado = data['results'][0]

            instrucciones = resultado['analyzedInstructions'][0]['steps'] if 'analyzedInstructions' in resultado and resultado['analyzedInstructions'] else []

            # Descripción del platillo
            descripcion_html = resultado.get('summary', "Descripción no disponible.")
            descripcion_texto = BeautifulSoup(descripcion_html, 'html.parser').get_text()

            pasos = [paso['step'] for paso in instrucciones]

            # Imagen del platillo
            imagen = resultado['image'] if 'image' in resultado else None

            info = {
                "descripcion": descripcion_texto,
                "pasos": pasos,
                "imagen": imagen
            }

            return info
        else:
            print("Platillo no encontrado.")
    except requests.exceptions.RequestException as e:
        print("Error al hacer la solicitud:", e)


app.run(debug=True)

