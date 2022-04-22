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


def lower(value):
    return value.lower()


cont = 1
x = 0
listop = []
listsenha = ["ABCDEFGHIJKLMNOPQRSTUVWXYZ", "abcdefghijklmnopqrstuvwxyz", "0123456789", "@#$%&!"]
for_pass = ""

while cont == 1:
    print("1- Gerar nova senha\n2- Consultar senha\n3- Apagar senha\n4- Sair")
    opcao = input()
    if isnumber(opcao):
        if int(opcao) == 1:
            print("Qual o tamanho da senha desejada?")
            tamanho_da_senha = input()
            if isnumber(tamanho_da_senha):
                print("A senha deve ser composta por letras maiúsculas?")
                listop.append(lower(input()))
                print("A senha deve ser composta por letras minusculas?")
                listop.append(lower(input()))
                print("A senha deve ser composta por numeros?")
                listop.append(lower(input()))
                print("A senha deve ser composta por símbolos?")
                listop.append(lower(input()))
                for x in range(3):
                    if listop[x] == "sim" or listop[x] == "s":
                        for_pass = for_pass + listsenha[x]
                password = "".join(random.sample(for_pass, int(tamanho_da_senha)))
                print(f"A senha é: {password}")
            else:
                print("Valor não válido")
                break
        if int(opcao) == 2:
            print("Ainda em construção")
        if int(opcao) == 3:
            print("Ainda em construção")
        if int(opcao) == 4:
            break
    else:
        print("Opção não válida")
        break
