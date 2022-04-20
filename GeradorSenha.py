"""
Gerador automático de senhas aleatórias
"""
import random


def isnumber(value):
    try:
        float(value)
    except ValueError:
        return False
    return True


lower_case = "abcdefghijklmnopqrstuvwxyz"
upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
symbols = "@#$%&!"

print("1- Gerar nova senha\n2- Consultar senha\n3- Apagar senha")
opcao = input()
if opcao == 1:
    print("Qual o tamanho da senha desejada?")
    tamanho_da_senha = input()
for_pass = lower_case + upper_case + numbers + symbols
password = "".join(random.sample(for_pass, tamanho_da_senha))
print(f"A senha é: {password}")
