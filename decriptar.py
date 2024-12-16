import os
import pyaes

file = open("alvo.txt.ransomwaretroll", "rb")
data = file.read()

aes = pyaes.AESModeOfOperationCTR(b"testeransomwares")
decrypted = aes.decrypt(data)


os.remove("alvo.txt.ransomwaretroll")

file = open("alvo.txt", "wb")
file.write(decrypted)
file.close()