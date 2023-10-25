import os

def modify_exe_string(exe_path):
    # Abre o arquivo EXE original para leitura de bytes binários
    with open(exe_path, 'rb') as exe_file:
        exe_data = exe_file.read()

    # Substitui "data\\" por "modf\\"
    modified_data = exe_data.replace(b'data\\', b'modf\\')

    # Cria um novo arquivo EXE com a string modificada
    new_exe_path = "kd2modlauncher.exe"
    with open(new_exe_path, 'wb') as new_exe_file:
        new_exe_file.write(modified_data)

    return new_exe_path

def main():
    exe_path = "koumajou2.exe"
    new_exe_path = modify_exe_string(exe_path)

if __name__ == "__main__":
    main()
