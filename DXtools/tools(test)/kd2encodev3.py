import os
import struct

def create_dat_file(dat_file_name, folder_name):
    # Defina os tamanhos dos elementos de cabeçalho e de arquivo
    header_size = 48
    file_table_entry_size = 64
    directory_table_entry_size = 32

    # Inicialize as contagens
    num_files = 0
    num_directories = 0

    # Crie uma lista para armazenar os cabeçalhos de arquivo
    file_headers = []

    # Abra o arquivo .dat para escrita em modo binário
    with open(dat_file_name + ".dat", "wb") as dat_file:
        # Escreva a assinatura "DX"
        dat_file.write(b'DX')
        
        # Escreva a versão como um valor uint16 (6)
        dat_file.write(struct.pack("<H", 6))

        # Reserve espaço para o tamanho do tail (será preenchido posteriormente)
        tail_size_offset = dat_file.tell()
        dat_file.write(b'\x00' * 4)

        # Escreva os valores iniciais de endereços
        data_start_address = header_size
        filename_table_start_address = 0  # Será preenchido posteriormente
        file_table_start_address = 0  # Será preenchido posteriormente
        directory_table_start_address = 0  # Será preenchido posteriormente
        code_page = 1252

        dat_file.write(struct.pack("<Q", data_start_address))
        dat_file.write(struct.pack("<Q", filename_table_start_address))
        dat_file.write(struct.pack("<Q", file_table_start_address))
        dat_file.write(struct.pack("<Q", directory_table_start_address))
        dat_file.write(struct.pack("<Q", code_page))

        # Percorra todos os arquivos na pasta especificada
        for root, _, files in os.walk(folder_name):
            for file_name in files:
                file_path = os.path.join(root, file_name)
                num_files += 1

                # Leia o conteúdo do arquivo
                with open(file_path, "rb") as current_file:
                    file_data = current_file.read()

                # Crie o cabeçalho do arquivo
                filename = os.path.basename(file_name).encode('utf-8')
                filename_upper = filename.upper()
                filename_length = len(filename_upper)
                num_packs = (filename_length + 3) // 4

                file_header = struct.pack("<HH", num_packs, 0)
                file_header += filename_upper + b'\x00' * (4 - (filename_length % 4))
                file_header += filename + b'\x00' * (4 - (filename_length % 4))

                file_headers.append(file_header)

                # Escreva os dados do arquivo no arquivo .dat
                dat_file.write(file_data)

        # Calcule o tamanho do tail
        tail_size = (num_files + 1) * file_table_entry_size
        tail_size += (num_files + 1) * (filename_length + 8)  # tamanho das entradas de tabela de arquivo
        tail_size += num_directories * directory_table_entry_size

        # Preencha o tamanho do tail no cabeçalho
        dat_file.seek(tail_size_offset)
        dat_file.write(struct.pack("<I", tail_size))

        # Escreva a tabela de arquivos
        for header in file_headers:
            dat_file.write(header)

        # Escreva a tabela de diretórios

    print(f"Arquivo {dat_file_name}.dat criado com sucesso!")

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 3:
        print("Uso: python criar_arquivo_dat.py <nome_arquivo_dat> <pasta>")
    else:
        create_dat_file(sys.argv[1], sys.argv[2])
