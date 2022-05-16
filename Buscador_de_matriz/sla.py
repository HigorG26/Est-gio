import numpy as np
from buscasGeral import *


def select(arr):
    opcao = input('\n\nO que deseja buscar?\n1. Nome\n2. Idade\n3. Posição\n')
    if opcao == '1' or 'Nome' or 'nome':
        sNome(opcao, arr)
    elif opcao == '2' or 'Idade' or 'idade':
        sIdade(opcao, arr)
    elif opcao == '3' or 'Posição' or 'posição':
        sPos(opcao, arr)
    else:
        print('Opção inválida')
        select(arr)
        
def insere(arr):
##    continua = 'SIM'
##    while continua == 'SIM':
##        nome = input('Seu nome: ')
##        idade = int(input('Sua idade: '))
##        continua = input('Deseja adicionar mais?\n')
##        if continua == 'Não' or 'não' or 'nao' or 'n':
##            mod(nome, idade, arr, vc="não")
##        else:
##            continue

    while True:
        try:
            nome = input("Insira seu nome: ")
            idade = int(input("Informe sua idade: "))
            var_controle = input("Deseja adicionar mais alguém?\n")
            mod(nome,idade,arr,var_controle)
        except:
            print("Inválido.")
            sair = input("Deseja sair? ")
            if sair == "sair":
                exit
            else:
                continue
                

def mod(nome, idade, arr, vc):
    if vc == "sim" or "Sim":
        nome = nome.upper()
        dados = [nome, idade]
        arr.insert(-1, dados)
        insere(arr)
    else:
        nome = nome.upper()
        dados = [nome, idade]
        arr.insert(-1, dados)
        select(arr)

arrMain = []
insere(arrMain)
