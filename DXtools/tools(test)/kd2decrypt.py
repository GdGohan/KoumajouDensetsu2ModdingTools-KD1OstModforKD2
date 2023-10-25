import sys

def xor_decrypt(input_file, output_file, xor_key):
    with open(input_file, 'rb') as encrypted_file:
        encrypted_data = bytearray(encrypted_file.read())
    
    decrypted_data = bytearray(len(encrypted_data))

    for i in range(len(encrypted_data)):
        decrypted_data[i] = encrypted_data[i] ^ xor_key[i % len(xor_key)]

    with open(output_file, 'wb') as decrypted_file:
        decrypted_file.write(decrypted_data)

if len(sys.argv) != 2:
    print("Uso: python decrypt.py <arquivo_entrada>")
    sys.exit(1)

input_file = sys.argv[1]
output_file = input_file + "_decrypted"
xor_key = bytearray([0xEF, 0xC1, 0x20, 0x01, 0xDC, 0xF7, 0xBB, 0x72, 0xFA, 0xCB, 0xF2, 0x01])

xor_decrypt(input_file, output_file, xor_key)
print(f"Arquivo descriptografado salvo em {output_file}")
