import tkinter as tk
from tkinter import filedialog
import os

languages_list = None
previous_language = None
selected_language_label = None  # Adicione uma variável para o rótulo de idioma selecionado

def select_language_folder(selected_language):
    folder_path = filedialog.askdirectory(title="Selecione a pasta de idioma")
    if folder_path:
        update_language_list(folder_path, selected_language)

def update_language_list(folder_path, selected_language):
    global languages_list, previous_language, selected_language_label

    selected_language.set(folder_path)

    if previous_language:
        os.rename(os.path.join("modf/language", "custom"), previous_language)

    custom_path = os.path.join("modf/language", "custom")
    os.rename(folder_path, custom_path)

    previous_language = folder_path

    load_languages()

    # Atualize o rótulo do idioma selecionado
    language_name = os.path.basename(folder_path)
    selected_language_label.config(text=f"Custom ({language_name})")

def load_languages():
    languages_list.delete(0, tk.END)
    for language in os.listdir("modf/language"):
        language_path = os.path.join("modf/language", language)
        if os.path.isdir(language_path):
            languages_list.insert(tk.END, language)

def main():
    global languages_list, previous_language, selected_language_label

    window = tk.Tk()
    window.title("Mod Launcher")

    selected_language = tk.StringVar()

    select_button = tk.Button(window, text="Selecione a pasta de idioma", command=lambda: select_language_folder(selected_language))
    select_button.pack()

    languages_list = tk.Listbox(window)
    languages_list.pack()

    load_languages()

    # Adicione um rótulo para mostrar o idioma selecionado
    selected_language_label = tk.Label(window, text="Custom")
    selected_language_label.pack()

    window.mainloop()

if __name__ == "__main__":
    main()
