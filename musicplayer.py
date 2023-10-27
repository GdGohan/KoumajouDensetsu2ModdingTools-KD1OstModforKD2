import os
import tkinter as tk
from tkinter import Listbox, Button, Scale
import pygame
import threading

d_f = "./"
music_folder = "modf/bgm"
define_folder = "modf/define"
music_playing = None
loop_start = 0
loop_end = 0

def load_music_info():
    music_info = {}
    with open(os.path.join(d_f, define_folder, "bgmlist.txt"), "r", encoding="shift_jis") as file:
        lines = file.read().splitlines()
        in_bgm_section = False
        for line in lines:
            line = line.strip()
            if not line or line.startswith("//"):
                continue
            if line == "[bgm]":
                in_bgm_section = True
                continue
            if in_bgm_section:
                parts = line.split(",")
                if len(parts) == 4:
                    name, start_sample, end_sample, music_name = parts
                    equals_index = name.find("=")
                    if equals_index != -1:
                        name = name[equals_index + 1:]
                    music_info[name] = {
                        "name": music_name.strip(),
                        "start_sample": int(start_sample),
                        "end_sample": int(end_sample)
                    }
    return music_info

def load_music_files(music_info):
    music_files = []
    for key, value in music_info.items():
        if key != "bgm_total":
            music_name = value["name"]
            loop_start = value["start_sample"] / 44100.0  # Convertendo para segundos
            loop_end = value["end_sample"] / 44100.0  # Convertendo para segundos
            loop_file = os.path.join(d_f, music_folder, f"{key}")
            music_files.append({"loop_file": loop_file, "name": music_name, "loop_start": loop_start, "loop_end": loop_end})
    return music_files

def play_selected_music():
    selected_item = music_listbox.curselection()
    if selected_item:
        selected_item = selected_item[0]
        selected_music = music_files[selected_item]
        play_music(selected_music, progress_bar)

def play_music(selected_music, progress_bar):
    pygame.mixer.init()
    pygame.mixer.music.load(selected_music["loop_file"])
    global music_playing, loop_start, loop_end
    music_playing = selected_music
    loop_start = selected_music["loop_start"]
    loop_end = selected_music["loop_end"]
    pygame.mixer.music.play()
    progress_bar.config(to=1.1)  # Configurar a barra de progresso para 0-1

def pause_music():
    pygame.mixer.music.pause()

def resume_music():
    pygame.mixer.music.unpause()

def reset_music_to_start():
    global music_playing
    while music_playing:
        current_time = pygame.mixer.music.get_pos() / 1000.0
        if current_time >= loop_end:
            # Quando estiver próximo do final do loop, retorne ao ponto de início do loop
            pygame.mixer.music.set_pos(loop_start)

def check_end_sample():
    global music_playing
    while music_playing:
        current_time = pygame.mixer.music.get_pos() / 1000.0
        if current_time >= loop_end:
            # Chame a função para resetar a música ao ponto de início
            reset_music_to_start()

def update_progress(progress_bar):
    while True:
        if music_playing:
            progress = pygame.mixer.music.get_pos() / 1000.0
            progress_percentage = progress / (loop_end - loop_start)
            progress_bar.set(progress_percentage)
            
            if progress_percentage >= 1.0:
                pygame.mixer.music.set_pos(loop_start)  # Definir a posição de reprodução para o início do loop
                play_selected_music()

if __name__ == "__main__":
    music_info = load_music_info()
    music_files = load_music_files(music_info)

    root = tk.Tk()
    root.title("Music Player")

    music_listbox = Listbox(root)
    for music in music_files:
        music_listbox.insert(tk.END, music["name"])
    music_listbox.pack()

    progress_bar = Scale(root, from_=0, to=1, resolution=0.01, orient="horizontal", label="Progress")
    progress_bar.pack()

    play_button = Button(root, text="Play Music", command=play_selected_music)
    play_button.pack()

    pause_button = Button(root, text="Pause", command=pause_music)
    pause_button.pack()

    resume_button = Button(root, text="Resume", command=resume_music)
    resume_button.pack()

    # Inicie uma thread para verificar o fim do loop
    end_sample_thread = threading.Thread(target=check_end_sample)
    end_sample_thread.daemon = True
    end_sample_thread.start()

    # Inicie uma thread para atualizar a barra de progresso
    progress_thread = threading.Thread(target=update_progress, args=(progress_bar,))
    progress_thread.daemon = True
    progress_thread.start()

    root.mainloop()
