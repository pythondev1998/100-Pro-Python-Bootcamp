API_KEY = '0f3b8966164348c0963ad946b07df4e0'


"""Model
title
image
sourceUrl
analyzedInstructions (steps)
nutrition (calories, fat, carbs, protein)
"""

#TODO Search bar - Buscar el platillo

#TODO Mostrar lo buscado


import requests

API_KEY = '0f3b8966164348c0963ad946b07df4e0'

def obtener_info_platillo(platillo):
    url = f'https://api.spoonacular.com/recipes/complexSearch?query={platillo}&apiKey={API_KEY}&instructionsRequired=true&addRecipeNutrition=true'

    try:
        response = requests.get(url)
        data = response.json()

        if 'results' in data and len(data['results']) > 0:
            resultado = data['results'][0]

            titulo = resultado['title']
            imagen = resultado['image']
            source_url = resultado['sourceUrl'] if 'sourceUrl' in resultado else "URL de origen no disponible."
            instrucciones = resultado['analyzedInstructions'][0]['steps'] if 'analyzedInstructions' in resultado and resultado['analyzedInstructions'] else []

            nutrition = resultado['nutrition'] if 'nutrition' in resultado else {}
            calorias = nutrition['calories'] if 'calories' in nutrition else "Información nutricional no disponible."
            grasa = nutrition['fat'] if 'fat' in nutrition else "Información nutricional no disponible."
            carbohidratos = nutrition['carbs'] if 'carbs' in nutrition else "Información nutricional no disponible."
            proteina = nutrition['protein'] if 'protein' in nutrition else "Información nutricional no disponible."

            print("Título:", titulo)
            print("Imagen:", imagen)
            print("URL de origen:", source_url)
            print("Pasos de preparación:")
            if instrucciones:
                for paso in instrucciones:
                    print("  ", paso['step'])
            else:
                print("  No se encontraron instrucciones de preparación.")
            print("Detalles nutricionales:")
            print("  Calorías:", calorias)
            print("  Grasa:", grasa, "g")
            print("  Carbohidratos:", carbohidratos, "g")
            print("  Proteína:", proteina, "g")

            # Ingredientes
            if 'missedIngredients' in resultado:
                print("\nIngredientes faltantes:")
                for ingrediente in resultado['missedIngredients']:
                    print("  ", ingrediente['original'])

            if 'usedIngredients' in resultado:
                print("\nIngredientes utilizados:")
                for ingrediente in resultado['usedIngredients']:
                    print("  ", ingrediente['original'])

            if 'unusedIngredients' in resultado:
                print("\nIngredientes no utilizados:")
                for ingrediente in resultado['unusedIngredients']:
                    print("  ", ingrediente['original'])

            # Descripción del platillo
            if 'summary' in resultado:
                print("\nDescripción del platillo:")
                print(resultado['summary'])

        else:
            print("Platillo no encontrado.")
    except requests.exceptions.RequestException as e:
        print("Error al hacer la solicitud:", e)

if __name__ == "__main__":
    platillo_ingresado = input("Ingresa el nombre del platillo: ")
    obtener_info_platillo(platillo_ingresado)
