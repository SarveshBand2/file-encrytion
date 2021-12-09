#To encrypt file 
from cryptography.fernet import Fernet

key= ""

#file name
file = " "

#emncrypted file name
file_e = " "

#path of log file where it'll be saved
file_path = ""
extend ="\\"

file_merge = file_path + extend


# Encrypt files
files_to_encrypt = [file_merge + file]
encrypted_file_names = [file_merge + file_e]

count = 0

for encrypting_file in files_to_encrypt:

    with open(files_to_encrypt[count], 'rb') as f:
        data = f.read()

    fernet = Fernet(key)
    encrypted = fernet.encrypt(data)

    with open(encrypted_file_names[count], 'wb') as f:
        f.write(encrypted)


    count += 1
