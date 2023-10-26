import tkinter as tk
import os
import subprocess
import sys

def read_language_from_txt():
    if os.path.exists("selected_language.txt"):
        with open("selected_language.txt", "r") as file:
            return file.read().strip()
    return None

def rename_bckp_folder():
    language = read_language_from_txt()
    if language:
        bckp_folder = os.path.join("modf/language", "custom")
        os.rename(bckp_folder, os.path.join("modf/language", language))
        main()

languages_list = None
previous_language = None
selected_language_label = None


def select_language(selected_language):
    selected_item = languages_list.get(languages_list.curselection())
    if selected_item:
        selected_language.set(selected_item)
        update_language_list(selected_item, selected_language)
        save_language_to_txt(selected_item)  # Salvar o idioma selecionado no arquivo de texto

def update_language_list(selected_item, selected_language):
    global previous_language, selected_language_label

    selected_language_folder = os.path.join("modf/language", selected_item)

    if previous_language:
        os.rename(os.path.join("modf/language", "custom"), previous_language)

    custom_path = os.path.join("modf/language", "custom")
    os.rename(selected_language_folder, custom_path)

    previous_language = selected_language_folder

    selected_language_label.config(text=f"Custom ({selected_item})")

def load_languages():
    languages_list.delete(0, tk.END)
    language_folders = os.listdir("modf/language")
    for language in language_folders:
        if os.path.isdir(os.path.join("modf/language", language)):
            languages_list.insert(tk.END, language)

def save_language_to_txt(selected_language):
    with open("selected_language.txt", "w") as file:
        file.write(selected_language)

def main():
    global languages_list, previous_language, selected_language_label
    
    custom_folder = os.path.join("modf/language", "custom")
    if os.path.exists(custom_folder):
        rename_bckp_folder()  # Renomeia a pasta "bckp" se o idioma estiver no arquivo de texto
    else:
        window = tk.Tk()
        window.title("Mod Launcher")

        selected_language = tk.StringVar()

        languages_list = tk.Listbox(window)
        languages_list.pack()

        select_button = tk.Button(window, text="Selecionar idioma", command=lambda: select_language(selected_language))
        select_button.pack()

        load_languages()

        selected_language_label = tk.Label(window, text="Custom")
        selected_language_label.pack()

        custom_folder = os.path.join("modf/language", "custom")

        window.mainloop()

if __name__ == "__main__":
    main()
