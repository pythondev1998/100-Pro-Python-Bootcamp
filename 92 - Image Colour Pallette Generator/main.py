import os
from flask import Flask, render_template, request, jsonify, send_from_directory
from PIL import Image
import numpy as np
from sklearn.cluster import KMeans

app = Flask(__name__)

UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


def is_neutral_color(color):
    # Obtener los componentes RGB del color
    r, g, b = color

    # Calcular la diferencia entre los componentes RGB para detectar colores neutros
    color_difference = abs(r - g) + abs(g - b) + abs(b - r)

    # Si la diferencia es menor que un umbral, consideramos el color como neutro
    neutral_threshold = 50
    return color_difference < neutral_threshold

@app.route('/', methods=['GET', 'POST'])
def index():
    result = []
    image_url = None

    if request.method == 'POST':
        # Obtener la imagen cargada por el usuario
        uploaded_image = request.files['imageFile']

        # Verificar si se cargó un archivo válido
        if uploaded_image.filename != '':
            try:
                # Crear el directorio "uploads" si no existe
                if not os.path.exists(app.config['UPLOAD_FOLDER']):
                    os.makedirs(app.config['UPLOAD_FOLDER'])

                # Guardar la imagen en la carpeta de uploads
                filename = uploaded_image.filename
                filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
                uploaded_image.save(filepath)

                # Leer la imagen utilizando Pillow
                image = Image.open(filepath)

                # Procesar la imagen utilizando la función process_image
                result = process_image(image)

                # Obtener solo los primeros 10 colores
                result = result[:10]

                # Obtener la URL de la imagen cargada
                image_url = request.url_root + 'uploads/' + filename

                # Devolver la respuesta como un objeto JSON utilizando jsonify
                response_data = {
                    'result': result,
                    'image_url': image_url
                }

                # Agregar mensajes de registro para depuración
                print("Response data:", response_data)

                return jsonify(response_data)

            except Exception as e:
                result = str(e)

    return render_template('index.html', result=result, image_url=image_url)


# Función para servir las imágenes cargadas por los usuarios desde la carpeta "uploads"
@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

def process_image(image):
    # Convertir la imagen a un arreglo NumPy
    image_np = np.array(image)

    # Calcular el total de píxeles en la imagen
    total_pixels = image_np.shape[0] * image_np.shape[1]

    # Reorganizar el arreglo de la imagen a una matriz 2D (píxeles x 3 canales de color)
    reshaped_image = image_np.reshape(-1, 3)

    # Aplicar K-Means clustering para agrupar colores similares
    n_colors = 16  # Número de clusters
    kmeans = KMeans(n_clusters=n_colors, random_state=42)
    kmeans.fit(reshaped_image)

    # Obtener los centroides de los clusters
    colors = kmeans.cluster_centers_.astype(int)

    # Filtrar colores negros, grises y similares
    colors = [color for color in colors if not is_neutral_color(color)]

    # Calcular los porcentajes de cada color en la imagen
    color_counts = np.unique(kmeans.labels_, return_counts=True)[1]
    color_percentages = (color_counts / total_pixels) * 100

    # Crear una lista de diccionarios para almacenar la información de cada color
    color_info_list = []

    # Iterar sobre los colores únicos y sus porcentajes
    for color, percentage in zip(colors, color_percentages):
        # Convertir el color a código hexadecimal
        color_code = '#{:02x}{:02x}{:02x}'.format(*color)

        # Crear un diccionario con la información del color
        color_info = {
            'Color': color.tolist(),  # Convertir el color a una lista
            'Color Code': color_code,
            'Percentage': percentage
        }

        # Agregar el diccionario a la lista
        color_info_list.append(color_info)

    # Ordenar la lista por porcentajes descendentes
    color_info_list.sort(key=lambda x: x['Percentage'], reverse=True)

    print("Color Info List:", color_info_list)
    return color_info_list


if __name__ == '__main__':
    app.run(debug=True)
