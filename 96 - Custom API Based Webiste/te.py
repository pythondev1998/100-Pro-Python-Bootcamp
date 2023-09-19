import requests

API_KEY = '6fe10dc10bbb40f5a620cb732a7b7072'

def obtener_sugerencias_por_titulo(query):
    url = f'https://api.spoonacular.com/recipes/complexSearch?query={query}&apiKey={API_KEY}&instructionsRequired=true&addRecipeNutrition=true'

    response = requests.get(url)
    data = response.json()

    sugerencias = []

    if 'results' in data and len(data['results']) > 0:
        for resultado in data['results']:
            titulo = resultado['title']
            sugerencias.append(titulo)

    return sugerencias

# Ejemplo de uso
query = "Rice"
sugerencias = obtener_sugerencias_por_titulo(query)
print("Sugerencias:", sugerencias)
