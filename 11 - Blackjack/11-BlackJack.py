import random
from art import logo
#Variables y listas
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
cards_user = []
cards_machine = []

# Metodo para insertar cartas en la baraja
def cards_random(cantidad, direction):
  turno = random.sample(cards, cantidad)
  if(direction == "user"):
    for valor in turno:
        cards_user.append(valor)
  elif(direction == "pc"):
     for valor in turno:
        cards_machine.append(valor)

# Metodo | Reparte primera ronda
def first_round():
   cards_random(2,"user")
   print(f"Your cards: {cards_user}, current score: {sum(cards_user)}")
   cards_random(2,"pc")
   print(f"Computer's first card: {cards_machine[0]}")

# Metodo | Proximas rondas
def next_round():
   print(logo)
 
   turn = False

   if sum(cards_user) < 21:
      cont = input("Type 'y' to get another card, type 'n' to pass: ")
      if(cont == "y"):
         cards_random(1,"user")
         print(f"Your cards hand: {cards_user}, cuerrent score:{sum(cards_user)}")
         print(f"Computer's first card: {cards_machine[0]}")

         if(sum(cards_user) > 21):
            print(f"Your cards hand: {cards_user}, cuerrent score:{sum(cards_user)}")
            print(f"Computer's final hand: {cards_machine}, final score: {sum(cards_machine)}")
            print("You lose")
         else:
            next_round()

      elif(cont == "n"):
         while (sum(cards_machine) <= 17 and turn == False):
            cards_random(1,"pc")
            if (sum(cards_machine) > 17):
         
                if(sum(cards_machine) >21):
                  print("Yo win!")
                  print(f"Your final hand: {cards_user}, final score: {sum(cards_user)}")  
                  print(f"Computer's final hand: {cards_machine}, final score: {sum(cards_machine)}")
                  turn = True
                else:
                   print("You lose")
                   print(f"Your final hand: {cards_user}, final score: {sum(cards_user)}")  
                   print(f"Computer's final hand: {cards_machine}, final score: {sum(cards_machine)}")
         if (sum(cards_machine) == 21):
                  print("You lose")
                  print(f"Your final hand: {cards_user}, final score: {sum(cards_user)}")  
                  print(f"Computer's final hand: {cards_machine}, final score: {sum(cards_machine)}")



# Metodo primera pregunta 

resp = (input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")) 
if(resp == "y"):
   first_round()
   next_round()
else:
   print("Bye")
