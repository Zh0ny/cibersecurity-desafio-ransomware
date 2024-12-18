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

## chave para descriptografia
key = b"testeransomwares"
list_of_decrypt_data = []
for file_data in files_data:
    aes = pyaes.AESModeOfOperationCTR(key)
    list_of_decrypt_data.append(aes.decrypt(file_data))
## remover o arquivo criptografado
for file in archives: os.remove(file)

## criar o arquivo descriptografado
new_files = [file_name.replace(".ransomwarenewbie","") for file_name in archives]
new_files = [open(f'{file}','wb') for file in new_files] 
for i,file in enumerate(new_files): 
	file.write(list_of_decrypt_data[i])
for file in new_files: file.close()
