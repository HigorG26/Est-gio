def sNome(opcao, arr):
    x=0
    dadoEspecifico = input('\nQual nome deseja buscar?\n')
    for dado in arr[x]:
        if arr[x][0] == dadoEspecifico.upper():
            print(arr[x])
            break
        if dadoEspecifico not in arr:
            print('Nome não encontado dentro da tabela!')

def sIdade(opcao, arr):
    x=0
    dadoEspecifico = input('\nQual idade deseja buscar?\n')
    for dado in arr[x]:
        if arr[x][1] == dadoEspecifico:
            print(arr[x])
    if dadoEspecifico not in arr:
            print('Idade não encontada dentro da tabela!')
            
def sPos(opcao, arr):
    busca = int(input('Qual posição da lista deseja buscar?\n'))
    for dado in len(arr):
        if busca == dado:
            print(f'Dados: {arr}')
    if pos not in len(arr):
        print('Posição solicitada não está dentro da tabela!!')
