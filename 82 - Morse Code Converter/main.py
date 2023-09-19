# Diccionario con las equivalencias de caracteres a código Morse
morse_dict = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
    'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
    'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',
    'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--',
    'Z': '--..', '0': '-----', '1': '.----', '2': '..---', '3': '...--',
    '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..',
    '9': '----.', ' ': ' ' 
}

def string_to_morse(input_string):
    morse_code = ""
    for char in input_string.upper():
        if char in morse_dict:
            morse_code += morse_dict[char] + " "
        else:
            morse_code += char 
    return morse_code

def main():
    user_input = input("Enter a phrase or word: ")
    morse_result = string_to_morse(user_input)
    print("Result: ")
    print(morse_result)

if __name__ == "__main__":
    main()
