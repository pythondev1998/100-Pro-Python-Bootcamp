import random
from game_data import data
from art import logo, vs

# 1. Descomponer el problema en fragmentos

# El programa se trata de comparar dos personas segun quien
# Tenga mayor cantidad de seguidores (Comparar el campo de follower_count)
# Tambien se debe tomar en consideracion los aciertos para ir sumandolos 
# Y detener el programa cuando se falle
# Observacion es que se seguira comparando entre (A y B) si se acierta la A entonces
# Se compra la B con la C (nueva random)


# 2. Hacer una lista de los requerimientos (To Do List )

# - Compare A or B: Katy Perry, a Musician, from United States.(GetInfo) [Metodo]
# - Variable sumador. (Counter) [Variable]
# - Se necesita un metodo que compare a las dos personas
# - Importar los modulos y la data - Listo

# Metood para obtener la informacion (Una a la vez)
def GetInfo (option):
    list_dic = random.choice(data)
    name = list_dic["name"]
    description = list_dic["description"]
    country = list_dic["country"]

    if (option == True):
        print(f"Compare A: {name}, a {description}, from {country}")
    elif (option == False):
        print(f"Against B: {name}, a {description}, from {country}")
    else:
        print(f"Compare A: {name}, a {description}, from {country}")
    return list_dic

# Metodo para comparar a las dos personas
def Compare(guess,a_option, b_option):
    opt_a = a_option["follower_count"]
    opt_b = b_option["follower_count"]
    counter = 0
    acerto = ""
    if(opt_a > opt_b):
        if(guess == "A"):
            counter += 1
        else:
            print(f"Sorry, that's wrong. Final score: {counter}")
            acerto = "C"
        acerto = "A"
             
    elif(opt_a < opt_b):
        if(guess == "B"):
            counter += 1
               
        else:
            print(f"Sorry, that's wrong. Final score: {counter}")
            acerto = "C"
        acerto = "B"
    if acerto == "C":
        print("")
    else:
        if (acerto == "A"):
            secondRound(a_option, "A")
        else:
             secondRound(b_option, "B")
    
def secondRound(list, opt):
    if (opt == "A"): 
        a_option = GetInfo(list)
        print(vs)
        b_option = GetInfo(False)
    else:
        a_option = GetInfo(True)
        print(vs)
        b_option = GetInfo(list)
        guess = input("Who has more followers? Type 'A' or 'B': ")
        Compare(guess,a_option, b_option)

# Solicitud y repsuesta del usuario A or B
def startGame():
    print(logo)
    a_option = GetInfo(True)
    print(vs)
    b_option = GetInfo(False)
    guess = input("Who has more followers? Type 'A' or 'B': ")
    Compare(guess,a_option, b_option)
startGame()


