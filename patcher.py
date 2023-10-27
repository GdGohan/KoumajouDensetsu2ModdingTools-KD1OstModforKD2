import os

def modify_exe_string(exe_path, custom_name):
    # Abre o arquivo EXE original para leitura de bytes binários
    with open(exe_path, 'rb') as exe_file:
        exe_data = exe_file.read()

    # Substitui "data\\" por "modf\\"
    modified_data = exe_data.replace(b'data\\', b'modf\\')

    # Substitui "config.ini" por "confmf.ini"
    modified_data2 = modified_data.replace(b'config.ini', b'confmf.ini')

    # Converta o nome personalizado em bytes usando UTF-8
    custom_name_bytes = custom_name.encode('utf-8')

    # Substitui "custom" pelo nome personalizado fornecido pelo usuário
    modified_data3 = modified_data2.replace(b'Custom', custom_name_bytes)

    # Cria um novo arquivo EXE com a string modificada
    new_exe_path = "kd2modlauncher.exe"
    with open(new_exe_path, 'wb') as new_exe_file:
        new_exe_file.write(modified_data3)

    return new_exe_path

def main():
    exe_path = "koumajou2.exe"
    custom_name = input("Write the name of the custom language: ")
    new_exe_path = modify_exe_string(exe_path, custom_name)
    print(f"The modified EXE has been created at {new_exe_path}")

if __name__ == "__main__":
    main()
