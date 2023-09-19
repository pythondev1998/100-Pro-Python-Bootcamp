import requests
import random

# Función para contar las palabras en un texto
def count_words(text):
    if text is None:
        return 0
    words = text.split()
    return len(words)

# Reemplaza 'TU_CLAVE_DE_API' con tu clave de API de News API
api_key = '95afeb7482f04209bae9856e1289a6e4'

# URL de la API de News
url = f'https://newsapi.org/v2/top-headlines?country=us&apiKey={api_key}'

try:
    # Realizar la solicitud GET a la API de News
    response = requests.get(url)

    # Verificar si la solicitud fue exitosa
    if response.status_code == 200:
        data = response.json()

        # Obtener la lista de artículos
        articles = data['articles']

        # Inicializar una lista para almacenar los artículos seleccionados
        selected_articles = []

        # Mientras no se hayan seleccionado suficientes palabras
        while count_words(" ".join(selected_articles)) < 100 and articles:
            # Seleccionar un artículo aleatorio y eliminarlo de la lista
            random_article = random.choice(articles)
            articles.remove(random_article)

            # Obtener los datos del artículo
            title = random_article.get('title', '')
            author = random_article.get('author', '')
            description = random_article.get('description', '')
            content = random_article.get('content', '')

            # Combinar los campos de título, autor, descripción y contenido
            combined_content = f"{title} {author} {description} {content}"

            # Agregar el artículo a la lista de artículos seleccionados
            selected_articles.append(combined_content)

        # Si no se alcanzaron las 100 palabras, intentar seleccionar otro artículo
        if count_words(" ".join(selected_articles)) < 100 and articles:
            random_article = random.choice(articles)
            title = random_article.get('title', '')
            author = random_article.get('author', '')
            description = random_article.get('description', '')
            content = random_article.get('content', '')
            combined_content = f"{title} {author} {description} {content}"
            selected_articles.append(combined_content)

        # Imprimir los datos de los artículos seleccionados y el número total de palabras
        for idx, article in enumerate(selected_articles, 1):
            print(f"Artículo {idx}:")
            print(article)
            print("-" * 50)
        print(f"Número total de palabras en todos los artículos: {count_words(' '.join(selected_articles))}")

        if not selected_articles:
            print("No se encontraron artículos con suficientes palabras.")
    else:
        print("Error al realizar la solicitud a la API.")
except requests.exceptions.RequestException as e:
    print("Error de conexión:", e)
