import os

def main(dat_file_name, folder_name):
    # Caminho completo para o arquivo .dat
    dat_file_path = dat_file_name + ".dat"

    try:
        # Abre o arquivo .dat para escrita em modo binário
        with open(dat_file_path, "wb") as dat_file:
            # Adiciona os bytes 44 58 03 no início do arquivo
            dat_file.write(bytes([]))

            # Percorre todos os arquivos na pasta especificada
            for root, _, files in os.walk(folder_name):
                for file in files:
                    # Caminho completo para o arquivo atual
                    file_path = os.path.join(root, file)

                    # Lê o arquivo em bytes e escreve no arquivo .dat
                    with open(file_path, "rb") as current_file:
                        dat_file.write(current_file.read())

        print(f"Arquivo {dat_file_name}.dat criado com sucesso!")

    except Exception as e:
        print(f"Ocorreu um erro: {str(e)}")

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 3:
        print("Uso: python criar_arquivo_dat.py <nome_arquivo_dat> <pasta>")
    else:
        main(sys.argv[1], sys.argv[2])
