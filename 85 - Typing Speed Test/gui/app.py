import tkinter as tk
from tkinter import Button, Text
from data.data import get_articles, count_words
import time
import numpy as np
import requests
import random

class App:
    def __init__(self, root, user_input):
        self.root = root
        self.root.title("Typing Speed Test")
        self.user_input = user_input
        self.timer_running = False
        self.generated_text = ""  # Variable para almacenar el texto generado
        self.create_widgets()

    def create_widgets(self):
        self.text_area = Text(self.root, wrap=tk.WORD, font=("Arial", 12), height=10)
        self.text_area.pack(fill=tk.BOTH, expand=True)
        self.text_area.config(state=tk.DISABLED)  # Deshabilitar el área de texto

        self.generate_button = Button(self.root, text="Start Test", command=self.start_test)
        self.generate_button.pack(pady=10)

    def start_test(self):
        if not self.timer_running:
            self.generate_button.config(state=tk.DISABLED)  # Deshabilitar el botón "Start Test"
            self.user_input.enable_input()  # Habilitar el área de texto para el usuario
            self.user_input.clear_input()  # Limpiar el contenido del área de texto del usuario
            self.text_area.config(state=tk.NORMAL)  # Habilitar el área de texto generado
            self.text_area.delete("1.0", tk.END)  # Limpiar el área de texto generado
            self.text_area.insert(tk.END, "Generating text...\n")
            self.text_area.update_idletasks()  # Actualizar el área de texto

            # Obtener el texto generado automáticamente
            self.generated_text = " ".join(get_articles())  # Guardar el texto generado en el atributo

            self.text_area.delete("1.0", tk.END)  # Limpiar el área de texto generado
            self.text_area.insert(tk.END, self.generated_text + "\n")
            self.text_area.insert(tk.END, "-" * 50 + "\n")

            self.start_time = time.time()  # Tiempo de inicio del test
            self.timer_running = True  # Iniciar el temporizador

            # Iniciar el temporizador para deshabilitar el área de texto después de un minuto
            self.root.after(60000, self.finish_test)

    def finish_test(self):  # Movimos esta función dentro de la clase App
        self.timer_running = False  # Detener el temporizador
        self.user_input.disable_input()  # Deshabilitar el área de texto del usuario
        self.text_area.config(state=tk.DISABLED)  # Deshabilitar el área de texto generado
        self.generate_button.config(state=tk.NORMAL)  # Habilitar nuevamente el botón "Start Test"
        
        # Obtener el texto ingresado por el usuario
        user_text = self.user_input.get_input()

        # Calcular el tiempo transcurrido y las palabras ingresadas por minuto (WPM)
        elapsed_time = time.time() - self.start_time
        minutes = elapsed_time / 60
        words_per_minute = count_words(user_text) / minutes

        # Calcular el porcentaje de similitud entre el texto original y el texto ingresado por el usuario
        similarity_percentage = calculate_similarity_percentage(self.generated_text, user_text)

        # Calcular el puntaje (CPM) y el porcentaje de ranking
        cpm = count_words(user_text)
        ranking_percentage = 100 - similarity_percentage

        # Mostrar los resultados en el área de texto generado
        self.text_area.config(state=tk.NORMAL)  # Habilitar el área de texto generado
        self.text_area.insert(tk.END, "\n\n*** RESULTS ***\n")
        self.text_area.insert(tk.END, f"Elapsed time: {elapsed_time:.2f} seconds\n")
        self.text_area.insert(tk.END, f"Words per minute (WPM): {words_per_minute:.2f}\n")
        self.text_area.insert(tk.END, f"Your score: {cpm} CPM (that is {words_per_minute:.2f} WPM)\n")
        self.text_area.insert(tk.END, f"Your score beats or equals {ranking_percentage:.2f}% of all.\n")
        self.text_area.insert(tk.END, f"Similarity percentage: {similarity_percentage:.2f}%\n")
        incorrect_words = get_incorrect_words(self.generated_text, user_text)  # Agregamos esta línea para obtener incorrect_words
        self.text_area.insert(tk.END, f"Incorrect words: {', '.join(incorrect_words)}\n")
        self.text_area.insert(tk.END, "-" * 50 + "\n")
        self.text_area.config(state=tk.DISABLED)  # Deshabilitar el área de texto generado

def calculate_similarity_percentage(original_text, user_text):
    len_original = len(original_text)
    len_user = len(user_text)
    distance_matrix = np.zeros((len_original + 1, len_user + 1))

    for i in range(len_original + 1):
        for j in range(len_user + 1):
            if i == 0:
                distance_matrix[i][j] = j
            elif j == 0:
                distance_matrix[i][j] = i
            elif original_text[i-1] == user_text[j-1]:
                distance_matrix[i][j] = distance_matrix[i-1][j-1]
            else:
                distance_matrix[i][j] = 1 + min(distance_matrix[i-1][j], distance_matrix[i][j-1], distance_matrix[i-1][j-1])

    similarity = 100 * (1 - distance_matrix[len_original][len_user] / max(len_original, len_user))
    return similarity

def get_incorrect_words(original_text, user_text):
    # Convertir ambos textos en listas de palabras
    original_words = original_text.split()
    user_words = user_text.split()

    # Encontrar las palabras incorrectas
    incorrect_words = []
    for original_word, user_word in zip(original_words, user_words):
        if original_word != user_word:
            incorrect_words.append(user_word)

    return incorrect_words
