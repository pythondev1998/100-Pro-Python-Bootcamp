import tkinter as tk

class UserInput:
    def __init__(self, root):
        self.root = root
        self.user_input = tk.StringVar()
        self.create_widgets()

    def create_widgets(self):
        self.input_label = tk.Label(self.root, text="Ingresa tu texto:")
        self.input_label.pack()

        self.input_entry = tk.Entry(self.root, textvariable=self.user_input, width=50)
        self.input_entry.pack()

    def get_input(self):
        return self.user_input.get()

    def enable_input(self):
        self.input_entry.config(state=tk.NORMAL)

    def disable_input(self):
        self.input_entry.config(state=tk.DISABLED)

    def clear_input(self):
        self.user_input.set("")
