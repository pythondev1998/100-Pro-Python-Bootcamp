import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
List = []

print("Welcome to the PyPassword Generator!")
many_letters = int(input("How manny letters would you like in your password?"))
many_symbols = int(input("How manny symbols would you like?\n"))
many_numbers = int(input("How manny numbers would you like?\n"))
password = ""

for a in range (1,many_letters+1):
    Le = random.choice(letters)  
    List.append(Le)

for b in range (1,many_symbols+1):
    Sy = random.choice(symbols)  
    List.append(Sy)

for c in range (1,many_numbers+1):
    Nu = random.choice(numbers)  
    List.append(Nu)


random.shuffle(List)
password = "".join(List)
print(f"Your password is: {password}")