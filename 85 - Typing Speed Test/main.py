# Importar las clases y funciones necesarias
from gui.app import App
from gui.user_input import UserInput
import tkinter as tk

# Función principal para iniciar la aplicación
def main():
    # Crear la ventana raíz de la aplicación
    root = tk.Tk()

    # Iniciar el módulo para el input del usuario
    user_input = UserInput(root)

    # Iniciar la aplicación con el módulo de input del usuario
    app = App(root, user_input)

    # Iniciar el bucle principal de la interfaz gráfica
    root.mainloop()

# Verificar si este archivo es el punto de entrada principal
if __name__ == "__main__":
    main()
