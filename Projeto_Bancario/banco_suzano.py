from time import sleep

print('Seja Ben-vindo ao melhor banco do Brasil\n BANCO SUZANO\n')

nome_usuario = input('Qual é o seu nome?\n ')

deposito = saldo = limite = saque = cont = saldo_total = 0

while True:
    acao = input(f'\n{nome_usuario}, vou te passar algumas opções:\n 1 = Depósito\n 2 = Saque\n 3 = Extrato\n 0 = Sair\n ')
    # Depositando Valor
    if acao == '1':
        print('Opção escolhida é Depósito')
        valor = int(input('Qual valor deseja depositar? R$:'))
        deposito = valor
        # colocando uma condição que o valor de depósito precisa ser maior que zero
        if deposito > 0:
            print(f'O valor depósitado é R$:{deposito}')
            saldo = deposito
            saldo_total += saldo
            cont += 1
            print(f'Seu Saldo atual é R$:{saldo_total}')
            
        else:
            print('Seu valor precisa ser maior que 0\n')
            
    # Sacando Valor
    elif acao == '2': 
        print(f'Opção escolhida é Saque \nSeu saldo Atual é R$:{saldo_total}')
        #limintando em 3x o saque diário
        s = 0
        for c in range(0, 3):
            valor = int(input("Qual valor você quer sacar? R$:"))
            total = valor
            # colocando uma condição de o Valor do saque precisa ter disponível na conta
            if total < saldo_total:
                saldo_total -= total
                saque += 1
                if total > 500:
                    print('Esse Valor ultrapassou seu limite diário para saque')
                    exit()
                print(f"Parabens, você conseguiu sacar seu valor de R$:{total}!")
                print('-'* 30)
                print(f'Seu saldo Atual é R$:{saldo_total}')
                print('-'* 30)
                s +=1
                # querendo saber se ele quer continuar sacando
                resp = ' '
                while resp not in 'SN':
                    resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
                if resp == 'N':
                    break
            if total > saldo_total:
                    print(f"\nSaldo indisponível \nSeu Saldo Atual é R$:{saldo_total} \nTente novamente\n")
         
        if s >= 3:
            print(f'Limite de {s} saques diário foi esgotado')
            break
    # Vendo Extrato Bancário
    elif acao == "3":
        print('Opção escolhida é Extrato')
        print(f'Extrato da sua conta bancária: ')

    # Saindo da conta
    elif acao == '0':
        print('Certo')
        for c in range(3, 0, -1):
            sleep(2)
            print(c)
        break

    else:
        print(' Opção inválida\n Tente novamente\n')

print('\nObrigado, Volte sempre! ')