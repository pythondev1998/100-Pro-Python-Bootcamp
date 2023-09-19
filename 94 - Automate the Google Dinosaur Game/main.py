import time
from PIL import ImageGrab
import pyautogui
import os

# Obtener la ruta absoluta de la imagen de referencia
script_directory = os.path.dirname(os.path.abspath(__file__))
game_window_image = os.path.join(script_directory, "game_window_reference.png")

def locate_game_window():
    # Buscar el centro de la ventana del juego en la pantalla
    game_region = pyautogui.locateCenterOnScreen(game_window_image, grayscale=True)
    
    if game_region is None:
        print("Game window not found. Make sure the game is visible.")
        exit()

    # Obtener las coordenadas de la ventana del juego
    left = game_region[0] - 150  # Ajustar el ancho de la ventana
    top = game_region[1] - 25   # Ajustar la altura de la ventana
    right = game_region[0] + 150
    bottom = game_region[1] + 25

    return (left, top, right, bottom)

def has_obstacle(image):
    # Define the color threshold for obstacles (black color in the game)
    obstacle_color_threshold = 100

    # Analyze the pixels in the image
    for x in range(image.width):
        for y in range(image.height):
            pixel_color = image.getpixel((x, y))
            if sum(pixel_color) < obstacle_color_threshold:
                return True
    return False

def main():
    print("Starting T-Rex Game Automation...")
    time.sleep(3)  # Give some time to focus on the game window

    left, top, right, bottom = locate_game_window()

    while True:
        # Capture the game window region
        image = ImageGrab.grab(bbox=(left, top, right, bottom))

        # Check for obstacles
        if has_obstacle(image):
            # Press the space bar to jump
            pyautogui.press("space")
            print("Jumping!")

        # Small delay to avoid excessive processing
        time.sleep(0.1)

if __name__ == "__main__":
    main()
