import os

# Podemos usar o pass nas estruturas
# É possível usar o input no if

portifolio = [
    {'Chevrolet Tracker': 128},
    {'Chevrolet Onix': 98},
    {'Chevrolet Spin': 150},
    {'Hyundai HB20': 85},
    {'Hyundai Tucson': 120},
    {'Fiat Uno': 60},
    {'Fiat Nobi': 70},
    {'Fiat Pulse': 130}
]
# Poderia ter usado tuplas, teria sido mais fácil haha

alugados = []
continuar = 0

def mostrar_lista(lista):
    for idx, i in enumerate(lista):
        produto = list(i.items())
        nome, preco = produto[0]
        print(f'[{idx}] {nome} - R${preco} / dia')

while continuar == 0:
    print('=' * 15)
    print('Bem vindo à locadora de carros!')
    print('=' * 15)

    print('''
O que você deseja fazer?
0 - Mostrar portifólio | 1 - Alugar um carro | 2 - Devolver um carro''')
    opcao = int(input())
    while opcao != 0 and opcao != 1 and opcao != 2:
        print('As únicas opções disponíveis são 0, 1 e 2')
        opcao = int(input())
    os.system('cls')

    if opcao == 0:
        mostrar_lista(portifolio)
        print('')
        print('=' * 15)
        print('0 - CONTINUAR | 1 - SAIR')
        home = int(input())
        while home != 0 and home != 1:
            print('As únicas opções disponíveis são 0 e 1')
            home = int(input())
        if home == 0:
            os.system('cls')
            continue
        elif home == 1:
            break

    if opcao == 1:
        if len(portifolio) == 0:
            print('Não há carros a alugar')
        else:
            print('[ ALUGAR ] Dê uma olhada em nosso portifólio.')
            print('')
            mostrar_lista(portifolio)
            print('')
            print('Escolha o código do carro:')
            escolha = int(input())
            escolhido = portifolio[escolha]
            carro, valor = list(escolhido.items())[0]
            print('')
            print('Escolha por quantos dias deseja alugar:')
            dias = int(input())
            while dias < 1:
                print('A quantidade de dias deve ser maior que 0')
                dias = int(input())


            os.system('cls')
            print(f'Você escolheu {carro} por {dias} dias.')
            print(f'O aluguel totalizaria R${valor * dias}. Deseja alugar?')
            print('')
            print('=' * 15)
            print('0 - SIM | 1 - NÃO')
            alugar = int(input())
            while alugar != 0 and alugar != 1:
                print('As únicas opções disponíveis são 0 e 1')
                alugar = int(input())
            if alugar == 0:
                selecionado = portifolio.pop(escolha)
                alugados.append(selecionado)
                print(f'Parabéns! Você alugou o carro {carro} por {dias} dias.')
        print('')
        print('0 - CONTINUAR | 1 - SAIR')
        home = int(input())
        while home != 0 and home != 1:
            print('As únicas opções disponíveis são 0 e 1')
            home = int(input())
        if home == 0:
            os.system('cls')
            continue
        elif home == 1:
            break

    if opcao == 2:
        if len(alugados) == 0:
            print('Não há carros a devolver! ')
        else:
            print('Segue a lista de carros alugados. Qual você deseja devolver?')
            mostrar_lista(alugados)
            print('')
            print('=' * 15)
            print('')
            print('Escolha o código do carro que deseja devolver:')
            escolhido = int(input())
            devolver = alugados[escolhido]
            carro = list(devolver.keys())[0]
            devolvido = alugados.pop(escolhido)
            portifolio.append(devolvido)
            print(f'Obrigado por devolver o carro {carro}')
        print('')
        print('=' * 15)
        print('0 - CONTINUAR | 1 - SAIR')
        home = int(input())
        while home != 0 and home != 1:
            print('As únicas opções disponíveis são 0 e 1')
            home = int(input())
        if home == 0:
            os.system('cls')
            continue
        elif home == 1:
            break
