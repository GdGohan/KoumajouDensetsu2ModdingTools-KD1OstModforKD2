import os
import threading
from pydub import AudioSegment
from pydub.playback import play

d_f = "./"
# Caminho para a pasta que contém as músicas
music_folder = "modf/bgm"
define_folder = "modf/define"

# Carregue as informações do arquivo bgmlist.txt
def load_music_info():
    music_info = {}
    with open(os.path.join(d_f, define_folder, "bgmlist.txt"), "r", encoding="utf-8") as file:
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
                    # Encontre o índice do sinal de "=" e defina o nome a partir dele
                    equals_index = name.find("=")
                    if equals_index != -1:
                        name = name[equals_index + 1:]
                    music_info[name] = {
                        "name": music_name.strip(),
                        "start_sample": int(start_sample),
                        "end_sample": int(end_sample)
                    }
    return music_info

# Carregue as músicas e seus loops
def load_music_files(music_info):
    music_files = []
    for key, value in music_info.items():
        if key != "bgm_total":
            music_name = value["name"]
            loop_start = value["start_sample"]
            loop_end = value["end_sample"]
            loop_file = os.path.join(d_f, music_folder, f"{key}")
            music_files.append({"loop_file": loop_file, "name": music_name, "loop_start": loop_start, "loop_end": loop_end})
    return music_files

# Reproduza a música com loop
def play_music(music_info):
    def play_thread():
        audio = AudioSegment.from_ogg(music_info['loop_file'])
        looped_audio = audio[music_info['loop_start']:music_info['loop_end']]
        play(looped_audio)

    print(f"Reproduzindo: {music_info['name']}")
    threading.Thread(target=play_thread).start()

# Função para reproduzir a música selecionada
def play_selected_music(selected_item, music_files):
    if selected_item >= 1 and selected_item <= len(music_files):
        selected_music = music_files[selected_item - 1]
        play_music(selected_music)
    else:
        print("Seleção inválida. Escolha um número de música válido.")

# Carregar informações e arquivos de música
music_info = load_music_info()
music_files = load_music_files(music_info)

# Lista de músicas numeradas
for i, music in enumerate(music_files, start=1):
    print(f"{i}. {music['name']}")

# Solicitar ao usuário a seleção de música
while True:
    try:
        selected_item = int(input("Escolha o número da música para reproduzir (ou 0 para sair): "))
        if selected_item == 0:
            break
        play_selected_music(selected_item, music_files)
    except ValueError:
        print("Entrada inválida. Digite o número da música desejada.")