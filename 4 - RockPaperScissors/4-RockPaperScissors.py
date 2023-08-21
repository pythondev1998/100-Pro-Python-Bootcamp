import random

rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
game = [rock, paper, scissors]

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.")) #La persona
print(game[user_choice])

computer_choice = random.randint(0,2) #La maquina
print("Computer chose: ")
print(game[computer_choice])

if(user_choice == 0) and (computer_choice == 2):
    print("You win!")
elif(computer_choice == 0) and (user_choice == 2):
    print("You lose")
elif (user_choice > computer_choice):
    print("You win!")
elif (computer_choice > user_choice): 
    print("You lose")
elif(user_choice >= 3) and (user_choice < 0):
    print("You type an invalidad number")
elif (user_choice == computer_choice):
    print("It's a draw")


### Forma extensa

"""
game = [rock, paper, scissors]
import random

choose = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.") #La persona
num_random = str(random.randint(0,2)) #La maquina

if (choose == num_random):
    if(choose == "0"):
        print(rock) #Roca ambos
        print("Computer chose:" + rock + "Empate")
        
    elif(choose == "1"):
        print(paper) #Papel ambos
        print("Computer chose:" + paper + "Empate")
    else:
        print(scissors) #Tijeras ambos
        print("Computer chose:" + scissors + "Empate")

elif (choose == "0" and num_random == "1") or (choose == "1" and num_random =="0"):
    if (choose == 0):
        print(paper)#Ganaste
        print("Computer chose:" + rock + "Ganaste")
    else:
        print(rock)#Perdiste
        print("Computer chose:" + paper + "Perdiste")

elif (choose == "1" and num_random == "2") or (choose == "2" and num_random =="1"):
    if (choose == "1"):
        print(paper)#Perdiste
        print("Computer chose:" + scissors + "Perdiste")
    else:
        print(scissors)#Ganaste  
        print("Computer chose:" + paper + "Ganaste") 

elif (choose == "0" and num_random == "2") or (choose == "2" and num_random =="0"):
    if (choose == "0"):
        print(rock)#Ganaste
        print("Computer chose:" + scissors + "Ganaste")

    else:
        print(scissors)#Perdiste 
        print("Computer chose:" + rock + "Perdiste")
else:
    print("Error")

"""