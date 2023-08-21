# Read
# file = open("my_file.txt")
with open("my_file.txt") as file:
    contents = file.read()
    print(contents)
# file.close()

# Write
# w = write, a = append
# Si el archivo no existe, y se esta en el write mode se crea automaticamanete un archivo
with open("my_file.txt", mode="a") as file:
    file.write(" \nNew text")
