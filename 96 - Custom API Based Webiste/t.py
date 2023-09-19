from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

API_KEY = '6fe10dc10bbb40f5a620cb732a7b7072'

# Ruta para obtener sugerencias
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

# Ruta para la página principal
@app.route('/')
def index():
    return render_template('in.html')

if __name__ == '__main__':
    app.run(debug=True)
