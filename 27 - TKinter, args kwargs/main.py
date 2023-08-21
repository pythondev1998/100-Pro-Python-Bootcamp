from tkinter import *


def convert_miles_to_km():
    miles = float(input_field.get())
    km = miles * 1.60934
    km_label.config(text=f"{km:.2f}")

# Crear ventana principal
window = Tk()
window.title("Mile to KM Converter")
window.minsize(width=500, height=250)


# Crear etiquetas
miles_label = Label(text="Miles", font=("Arial", 18, "normal"))
miles_label.grid(row=0, column=0)

km_label = Label(text="KM", font=("Arial", 18, "normal"))
km_label.grid(row=1, column=0)

equal_label = Label(text="is equal to", font=("Arial", 18, "normal"))
equal_label.grid(row=1, column=1)

# Crear campo de entrada
input_field = Entry(width=10)
input_field.grid(row=0, column=1)

# Crear botón
convert_button = Button(text="Convert", command=convert_miles_to_km)
convert_button.grid(row=2, column=1)

# Ejecutar bucle principal
window.mainloop()