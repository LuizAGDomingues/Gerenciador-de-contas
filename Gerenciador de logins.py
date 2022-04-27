"""
Gerador automático de senhas aleatórias
"""
import getpass
import random
import os


def isnumber(value):
    try:
        float(value)
    except ValueError:
        return False
    return True


def lower(value):
    return value.lower()


def verifica(listaverificacao, senha):
    listpass = list(senha)
    verif = 0

    for familia in listaverificacao:
        listfamilia = list(familia)
        for letra in listfamilia:
            if letra not in listpass:
                verif = 1
            else:
                verif = 0
                break
        if verif == 1:
            return False
    return True


def gerarsenha(senha, tamanho):
    listop = []
    listsenha = ["ABCDEFGHIJKLMNOPQRSTUVWXYZ", "abcdefghijklmnopqrstuvwxyz", "0123456789", "@#$%&!"]
    for_pass = ""
    listverifica = []
    verificacao = 0

    print("A senha deve ser composta por letras maiúsculas?")
    listop.append(lower(input()))
    print("A senha deve ser composta por letras minusculas?")
    listop.append(lower(input()))
    print("A senha deve ser composta por numeros?")
    listop.append(lower(input()))
    print("A senha deve ser composta por símbolos?")
    listop.append(lower(input()))
    for x in range(4):
        if listop[x] == "sim" or listop[x] == "s":
            for_pass = for_pass + listsenha[x]
            listverifica.append(listsenha[x])
    while verificacao == 0:
        senha = "".join(random.sample(for_pass, int(tamanho)))
        if verifica(listverifica, senha):
            break
    print(f"A senha é: {senha}")
    listverifica.clear()
    listop.clear()
    return senha


def consultar(mapa, sit):
    print(f"{sit} -> Usuário: {mapa[sit][0]} Senha: {mapa[sit][1]}\n")


def importardados():
    dicionario = {}
    dados = open(f"C:/Users/{getpass.getuser()}/AppData/Local/Gerenciador de Logins/Banco_de_Dados.txt", "r")
    lista = list(dados)
    if lista == "":
        return dicionario
    else:
        for x in lista:
            lista2 = x.split()
            dicionario[lista2[0]] = [lista2[3], lista2[5]]
        return dicionario


cont1 = 1
cont1_1 = 1
cont1_2 = 1
cont1_3 = 1
password = ""
try:
    os.mkdir(f"C:/Users/{getpass.getuser()}/AppData/Local/Gerenciador de Logins")
except FileExistsError:
    print(f"Bem vindo de volta {getpass.getuser()}")
try:
    doc = open(f"C:/Users/{getpass.getuser()}/AppData/Local/Gerenciador de Logins/Banco_de_Dados.txt", "r")
except FileNotFoundError:
    doc = open(f"C:/Users/{getpass.getuser()}/AppData/Local/Gerenciador de Logins/Banco_de_Dados.txt", "w")
gerenciador = importardados()
while cont1 == 1:
    print("1- Gerar novo login\n2- Consultar login\n3- Apagar\n4- Sair")
    opcao = input()
    if isnumber(opcao):
        if int(opcao) == 1:
            while cont1_1 == 1:
                print("Informe o site para qual criará o login: ")
                site = lower(input())
                if site in gerenciador:
                    print("Já existe login para este site, deseja consultar?")
                    consul = lower(input())
                    if consul == "sim" or consul == "s":
                        consultar(gerenciador, site)
                        break
                    else:
                        break
                else:
                    print("Digite o usuário para login:")
                    usuario = input()
                    print("1- Digitar nova senha\n2- Gerar nova senha")
                    escolha = input()
                    if isnumber(escolha) and int(escolha) == 1:
                        print("Digite a senha:")
                        password = input()
                        gerenciador[site] = [usuario, password]
                        doc = open(f"C:/Users/{getpass.getuser()}/AppData/Local/Gerenciador de "
                                   f"Logins/Banco_de_Dados.txt", "a")
                        novo = f"{site} -> Usuário: {usuario} Senha: {password}\n"
                        doc.write(novo)
                        break
                    elif isnumber(escolha) and int(escolha) == 2:
                        print("Qual o tamanho da senha desejada?")
                        tamanho_da_senha = input()
                        if isnumber(tamanho_da_senha):
                            password = gerarsenha(password, tamanho_da_senha)
                            gerenciador[site] = [usuario, password]
                            doc = open(f"C:/Users/{getpass.getuser()}/AppData/Local/Gerenciador de "
                                       f"Logins/Banco_de_Dados.txt", "a")
                            novo = f"{site} -> Usuário: {usuario} Senha: {password}\n"
                            doc.write(novo)
                            break
                        else:
                            print("Valor não válido")
                            break
                    else:
                        print("Valor não válido")
                        break
        elif int(opcao) == 2:
            while cont1_2 == 1:
                if not bool(gerenciador):
                    print("Não há logins catalogados")
                    break
                else:
                    print("1- Consultar todas os logins catalogados\n2- Consultar login especifico")
                    escolha2 = input()
                    if isnumber(escolha2) and int(escolha2) == 1:
                        for chave in gerenciador.keys():
                            print(f"{chave} -> Usuário: {gerenciador[chave][0]} Senha: {gerenciador[chave][1]}")
                        break
                    elif isnumber(escolha2) and int(escolha2) == 2:
                        print("Digite o site para qual deseja consultar o login:")
                        site = lower(input())
                        if site not in gerenciador:
                            print("Login não existe para este site")
                            break
                        else:
                            consultar(gerenciador, site)
                            break
                    else:
                        print("Opção não válida")
                        break
        elif int(opcao) == 3:
            while cont1_3 == 1:
                print("1- Apagar todo o conteudo\n2- Apagar login especifico")
                escolha3 = input()
                if isnumber(escolha3) and int(escolha3) == 1:
                    gerenciador.clear()
                    print("Todos os dados foram apagados")
                    break
                elif isnumber(escolha3) and int(escolha3) == 2:
                    print("Digite o site que deseja apagar o login")
                    site = lower(input())
                    if site not in gerenciador:
                        print("Login não existe para este site")
                        break
                    else:
                        del gerenciador[site]
                        print(f"O login de {site} foi apagado")
                        break
                else:
                    print("Opção não válida")
                    break
        elif int(opcao) == 4:
            doc = open(f"C:/Users/{getpass.getuser()}/AppData/Local/Gerenciador de "
                       f"Logins/Banco_de_Dados.txt", "w")
            for y in gerenciador.keys():
                novo = f"{y} -> Usuário: {gerenciador[y][0]} Senha: {gerenciador[y][1]}\n"
                doc.write(novo)
            break
        else:
            print("Opção não válida")
            break
    else:
        print("Opção não válida")
        break
