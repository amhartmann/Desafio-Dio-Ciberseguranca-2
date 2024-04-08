import os
import pyaes

## Abrindo o arquivo alvo
file_name = "alvoseuarquivocriptografado.txt"
file = open(file_name, "rb")
file_data = file.read()
file.close()

## Chave para descriptografia
key = b"senhaparaencriptaredecriptaralvo"
aes = pyaes.AESModeOfOperationCTR(key)
decrypt_data = aes.decrypt(file_data)

## Removendo arquivo criptografado
os.remove(file_name)

## Recriando arquivo descriptografado
new_file = "alvo.txt"
new_file = open(f'{new_file}', "wb")
new_file.write(decrypt_data)
new_file.close()