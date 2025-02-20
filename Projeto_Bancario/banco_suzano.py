from time import sleep

print('Seja Bem-vindo ao melhor banco do Brasil\n BANCO SUZANO\n')

nome_usuario = input('Qual é o seu nome?\n ')

saldo_total = 0
saques_realizados = 0
LIMITE_SAQUES = 3  #limintando em 3 saques diário
historico_depositos = []  
historico_saques = []  

while True:
    acao = input(f'\n{nome_usuario}, vou te passar algumas opções:\n 1 = Depósito\n 2 = Saque\n 3 = Extrato\n 0 = Sair\n ')

    # Depositando valor
    if acao == '1':
        print('Opção escolhida: Depósito')
        valor = int(input('Qual valor deseja depositar? R$: '))
        # colocando uma condição que o valor de depósito precisa ser maior que zero
        if valor > 0:
            saldo_total += valor
            historico_depositos.append(valor)  # <<-- historicos das transaçoes de deposito
            print(f'O valor depositado foi R$:{valor}')
            print('-' * 50)
            print(f'Seu saldo atual é R$:{saldo_total}')
            print('-' * 50)
        else:
            print('O valor do depósito precisa ser maior que 0\n')

    # Sacando Valor
    elif acao == '2': 
        print('-' * 50)
        print(f'Opção escolhida: Saque \nSeu saldo Atual é R$:{saldo_total}')
        print('¨' * 50)

        if saques_realizados >= LIMITE_SAQUES:
            print(" Você já atingiu o limite de 3 saques diários! Tente novamente amanhã.")
            continue  

        valor = int(input("Qual valor você quer sacar? R$: "))

        if valor > 500:
            print(' Esse valor ultrapassou seu limite de R$500 por saque. Tente um valor menor.')
            continue  

        if valor <= saldo_total:
            saldo_total -= valor  
            historico_saques.append(valor)  # <<-- historicos das transaçoes de saque
            saques_realizados += 1  
            print(f" Saque realizado com sucesso! Valor: R$:{valor}")
            print('-' * 50)
            print(f" Seu saldo atual é R$:{saldo_total}")
            print('-' * 50)
            print(f" Você ainda pode realizar {LIMITE_SAQUES - saques_realizados} saques hoje.")
        else:
            print('-' * 50)
            print(f" Saldo insuficiente! Seu saldo atual é R$:{saldo_total}. Tente um valor menor.")
            print('-' * 50)

    #  Vendo Extrato
    elif acao == "3":
        print('\n EXTRATO BANCÁRIO ')
        print('¨' * 50)
        print(f'Saldo Atual: R$:{saldo_total}\n')
        print('¨' * 50)

        print(' Depósitos Realizados:')
        if historico_depositos:
            for i, deposito in enumerate(historico_depositos, 1):
                print(f' {i}º depósito: R$:{deposito}')
        else:
            print(' Nenhum depósito realizado.')

        print('\n Saques Realizados:')
        if historico_saques:
            for i, saque in enumerate(historico_saques, 1):
                print(f' {i}º saque: R$:{saque}')
        else:
            print(' Nenhum saque realizado.')

    #  Saindo da conta
    elif acao == '0':
        print('Encerrando sua sessão...')
        for c in range(3, 0, -1):
            sleep(1)
            print(c)
        break

    else:
        print(' Opção inválida! Tente novamente.')

print('\nObrigado por usar o BANCO SUZANO! Volte sempre!')
