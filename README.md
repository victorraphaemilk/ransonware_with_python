# Sistema de Criptografia e Descriptografia de Arquivos

Este projeto implementa um sistema simples de **criptografia e descriptografia de arquivos** usando o módulo `pyaes` em Python. Ele simula operações de segurança que podem ser utilizadas para proteger dados sensíveis.

---

## **Descrição**

O sistema possui dois scripts:

1. **Criptografia**: 
   - Lê um arquivo, criptografa seus dados usando AES no modo CTR e salva com a extensão `.ransomwaretroll`.
   - Remove o arquivo original para garantir a segurança.

2. **Descriptografia**:
   - Lê o arquivo criptografado, descriptografa seus dados com a mesma chave usada na criptografia e restaura o arquivo original.
   - Remove o arquivo criptografado após a operação.

---

## **Requisitos**

Antes de usar o sistema, certifique-se de ter instalado o módulo `pyaes`:
```bash
pip install pyaes