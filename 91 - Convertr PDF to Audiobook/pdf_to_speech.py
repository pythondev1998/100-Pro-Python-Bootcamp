import os
import PyPDF2
import pyttsx3
import tkinter as tk
from tkinter import filedialog, messagebox

def extract_text_from_pdf(pdf_file):
    text = ""
    with open(pdf_file, "rb") as file:
        pdf_reader = PyPDF2.PdfReader(file)
        num_pages = len(pdf_reader.pages)
        for page_num in range(num_pages):
            page = pdf_reader.pages[page_num]
            text += page.extract_text()
    return text

def convert_text_to_speech(text, output_file):
    engine = pyttsx3.init()
    engine.save_to_file(text, output_file)
    engine.runAndWait()

def browse_pdf_file():
    file_path = filedialog.askopenfilename(filetypes=[("PDF Files", "*.pdf")])
    pdf_file_entry.delete(0, tk.END)
    pdf_file_entry.insert(0, file_path)

    # Configurar automáticamente la ruta de archivo de salida
    output_folder, _ = os.path.split(file_path)
    output_file_entry.delete(0, tk.END)
    output_file_entry.insert(0, os.path.join(output_folder, "output.mp3"))

def convert_to_speech():
    pdf_file = pdf_file_entry.get()
    output_file = output_file_entry.get()

    if not os.path.isfile(pdf_file):
        messagebox.showerror("Error", "El archivo PDF no existe.")
        return

    text = extract_text_from_pdf(pdf_file)
    convert_text_to_speech(text, output_file)

    messagebox.showinfo("Conversión completa", "Texto extraído y convertido a discurso. Archivo de salida guardado.")

if __name__ == "__main__":
    root = tk.Tk()
    root.title("PDF to Speech Converter")

    # Widgets
    pdf_file_label = tk.Label(root, text="Ruta del archivo PDF:")
    pdf_file_entry = tk.Entry(root, width=50)
    browse_button = tk.Button(root, text="Buscar PDF", command=browse_pdf_file)

    output_file_label = tk.Label(root, text="Ruta de archivo de salida (MP3):")
    output_file_entry = tk.Entry(root, width=50)

    convert_button = tk.Button(root, text="Convertir a Speech", command=convert_to_speech)

    # Grid layout
    pdf_file_label.grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)
    pdf_file_entry.grid(row=0, column=1, padx=5, pady=5, columnspan=2)
    browse_button.grid(row=0, column=3, padx=5, pady=5)

    output_file_label.grid(row=1, column=0, padx=5, pady=5, sticky=tk.W)
    output_file_entry.grid(row=1, column=1, padx=5, pady=5, columnspan=2)

    convert_button.grid(row=2, column=0, columnspan=4, padx=5, pady=10)

    root.mainloop()
