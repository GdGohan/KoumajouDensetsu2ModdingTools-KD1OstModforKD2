import os
import struct

def create_dat_file(dat_file_name, folder_name):
    # Defina os tamanhos dos elementos de cabeçalho e de arquivo
    header_size = 12

    num_files = 0

    # Abra o arquivo .dat para escrita em modo binário
    with open(dat_file_name + ".dat", "wb") as dat_file:
        # Escreva o cabeçalho personalizado
        custom_header = bytes.fromhex("")
        dat_file.write(custom_header)

        # Percorra todos os arquivos na pasta especificada
        for root, _, files in os.walk(folder_name):
            for file_name in files:
                file_path = os.path.join(root, file_name)
                num_files += 1

                # Leia o conteúdo do arquivo
                with open(file_path, "rb") as current_file:
                    file_data = current_file.read()

                # Escreva os dados do arquivo no arquivo .dat
                dat_file.write(file_data)

    print(f"Arquivo {dat_file_name}.dat criado com sucesso!")

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 3:
        print("Uso: python criar_arquivo_dat.py <nome_arquivo_dat> <pasta>")
    else:
        create_dat_file(sys.argv[1], sys.argv[2])
