import sys
import os  # Importe o módulo 'os' para manipulação de caminhos de arquivo

def xor_encrypt(input_file, output_file, xor_key):
    with open(input_file, 'rb') as plain_file:
        plain_data = bytearray(plain_file.read())

    encrypted_data = bytearray(len(plain_data))

    for i in range(len(plain_data)):
        encrypted_data[i] = plain_data[i] ^ xor_key[i % len(xor_key)]

    # Modifique o nome do arquivo de saída
    root, ext = os.path.splitext(output_file)
    output_file = f"{root}_encrypted{ext}"

    with open(output_file, 'wb') as encrypted_file:
        encrypted_file.write(encrypted_data)

if len(sys.argv) != 2:
    print("Uso: python encrypt.py <arquivo_entrada>")
    sys.exit(1)

input_file = sys.argv[1]
output_file = os.path.splitext(input_file)[0] + os.path.splitext(input_file)[1]
xor_key = bytearray([0xEF, 0xC1, 0x20, 0x01, 0xDC, 0xF7, 0xBB, 0x72, 0xFA, 0xCB, 0xF2, 0x01])

xor_encrypt(input_file, output_file, xor_key)
print(f"Arquivo criptografado salvo em {output_file}")
