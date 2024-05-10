import os 
import pyaes

#abre o arquivo criptografado 
file_name = "documento.txt.badthings"
file = open (file_name, "rb")
file_data = file.read()
file.close()

#chave para descriptografar
key = b"ransonwaresbad"
aes = pyaes.AESModeOfOperationCTR(key)
decrypt_data = aes.decrypt(file_data)

#remove o arquvio criptografado 
os.remove(file_name)

#criar o arquivo descriptografado
new_file = "doc.txt"
new_file = open(f'{new_file}', 'wb')
new_file.write(decrypt_data)        
new_file.close()

