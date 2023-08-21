import requests

def search_movies(title):
    api_key = ''  # Reemplaza esto con tu propia API key de TMDB
    base_url = 'https://api.themoviedb.org/3/search/movie'

    # Parámetros de la consulta
    params = {
        'api_key': api_key,
        'query': title
    }

    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()  # Lanza una excepción si hay un error en la respuesta

        # Obtenemos los resultados de la búsqueda
        results = response.json()['results']

        # Extraemos la información requerida de cada película
        movies = []
        for result in results:
            movie = {
                'title': result['title'],
                'img_url': result['poster_path'],
                'year': result['release_date'][:4],  # Obtenemos solo el año de la fecha de lanzamiento
                'description': result['overview']
            }
            movies.append(movie)

        return movies

    except requests.exceptions.RequestException as e:
        print('Error en la solicitud:', e)

# Ejemplo de uso
search_results = search_movies('Avengers')
for movie in search_results:
    print(movie)
