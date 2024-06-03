import time
usuario = 'Washington Medeiros'
saldo = 0
saques = []
depositos = []
limite_saque = 500
limite = 3
while True:
    menu = f"""
    ===== Menu Bancario =====
    1 -       Saque
    2 -      Deposito
    3 -      Extrato
    0 -       Sair
    ========================
    """
    print(menu)

    opcao = int(input('digite a opção desejada: \n'))

    if opcao == 1 :
        if limite >= 1:
            valor_saque = float(input('R${:.2f} Disponiveis para saque, Digite o valor desejado: R$'.format(saldo.__float__())))
            if valor_saque <= saldo and valor_saque <= limite_saque:
                print('saque realizado com sucesso! ')

                #subtrai o saque realizado do saldo
                saldo = saldo - valor_saque

               #guarda na lista de saques
                saques.append(valor_saque)

               #reduz 1 saque diario
                limite += -1
            elif valor_saque > saldo:
                print('saldo insuficiente')
            elif valor_saque > limite_saque:
                print('limite de saque é R$500')
        else:
            print('limite de saques atigindo')

    elif opcao == 2:
        #le o valor do deposito
        valor_deposito = float(input('Qual valor deseja depositar R$'))

        #guarda na lista valor deposito
        depositos.append(valor_deposito)

        #faz a soma com o saldo
        saldo += valor_deposito

        print('Deposito realizado com sucesso')
    elif opcao == 3:
        print('Depositos: ')
        # variavel que recebe a lista/ variavel q print a lista
        for deposito in depositos:
            print(f'R${deposito:.2f}')
        print('Saques:')
        for saque in saques:
            print(f'R${saque:.2f}')
        print(f'Saldo R${saldo:.2f}')
    elif opcao == 0:
        break
    else:
        print('Opção invalidade, por favor selecione novamenta a operação desejada.')
    time.sleep(1)

    pass


