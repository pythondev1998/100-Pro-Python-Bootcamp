import pyttsx3

def main():
    text = "Hola, esta es una prueba de síntesis de voz en español."

    engine = pyttsx3.init()

    # Configurar la voz en español
    engine.setProperty('voice', 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_ES-MX_SABINA_11.0')  # Ejemplo de voz en español para México

    # Realizar la síntesis de voz con la configuración establecida
    engine.say(text)
    engine.runAndWait()

if __name__ == "__main__":
    main()
