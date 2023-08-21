for number in range(1, 101):
    if number % 3 == 0 and number % 5 == 0:
        print(f"FizzBuzz")
    else:
        if number % 3 == 0:
            print(f"Fizz")
        elif number % 5 == 0:
            print(f"Buzz")
        else:
            print(number)

# 1. En este programa se busca la impresion del FizzBuzz
# 2. No me da un error en consola, pero si al momento de reproducir veo una incongruencia
# 3. La computadora esta leyendo perfectamente el mandato.
# 5. Hice uso del print para visualizar lo que me daba como salida e identifique era un error logico
# 9. El codigo fue corrido varias veces para determinar la falla