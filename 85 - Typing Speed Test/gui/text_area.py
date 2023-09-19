import tkinter as tk
from tkinter import scrolledtext

class ScrolledText(scrolledtext.ScrolledText):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)

        self.config(
            wrap=tk.WORD,
            font=("Arial", 12),
            relief=tk.SOLID,
            borderwidth=1
        )

        # Ajustar el tamaño del widget para que se adapte al contenido
        self.pack(fill=tk.BOTH, expand=True)

    def clear(self):
        self.delete("1.0", tk.END)

    def set_text(self, text):
        self.clear()
        self.insert(tk.END, text)
