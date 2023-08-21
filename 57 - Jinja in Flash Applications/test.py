import requests
name = "brian"
url_genero = f"https://api.genderize.io/?name={name}"
respuesta_genero = requests.get(url_genero).json()
genero = respuesta_genero.get('gender')
print(genero)

    # Obtener edad
url_edad = f"https://api.agify.io/?name={name}"
respuesta_edad = requests.get(url_edad).json()
edad = respuesta_edad.get('age')
print(edad)
