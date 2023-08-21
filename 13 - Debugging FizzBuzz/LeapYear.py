year = int(input("Which year do you want to check?"))

if year % 4 == 0:
  if year % 100 == 0:
    if year % 400 == 0:
      print("Leap year.")
    else:
      print("Not leap year.")
  else:
    print("Leap year.")
else:
  print("Not leap year.")
  

# 1. En este codigo se busca saber cuando un anio es biciesto
# 2. Al momento de correrlo me dice el formato no se esta convirtiendo de string
# 3. Pretendiendo ser la computadora me da por entender que no puedo leer una cadena de caracteres donde se esta comparando numeros
# 4. Arreglo el error permitiendo la conversion de int(year)