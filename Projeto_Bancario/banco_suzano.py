from time import sleep
from validate_docbr import CPF
import requests
import textwrap



cpf = []
saldo_total = 0
saques_realizados = 0
LIMITE_SAQUES = 3  #limintando em 3 saques diário
AGENCIA = "0001"
historico_depositos = []  
historico_saques = []  
usuarios = []
contas = []


def linha(tam=50):
    return'_' * 50



def cabeçalho(txt):
    print(linha())
    print(txt.center(50)) # centralizando o texto 
    print(linha())

# lendo a resposta como "int"
def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except(ValueError, TypeError):
            print('ERRO: por favor, digite um número inteiro valído.')
            continue
        except KeyboardInterrupt:
            print('Entrada de dados de dados interrompida pelo usuário.')
            return 0
        else:
            return n


def menu(lista):
    cabeçalho('Seja Bem-vindo ao melhor banco do Brasil\n              BANCO SUZANO\n')
    e = 1 
    for item in lista: # colocando as opções em ordem
        print(f'{e} - {item}')
        e += 1 
    print(linha())
    acao = leiaInt('Escolha uma das opções abaixo:\n')
    return acao


def deposito(historico_depositos, valor):
    if isinstance(historico_depositos, list):  # Verifica se é uma lista
        global saldo_total
        if valor > 0:
            saldo_total += valor  # Atualiza saldo localmente
            historico_depositos.append(valor)  # Adiciona ao histórico corretamente
            
            print(f'O valor depositado foi R$:{valor}')
            print('-' * 50)
            print(f'Seu saldo atual é R$:{saldo_total}')
            print('-' * 50)
            return saldo_total
        else:
            print('O valor do depósito precisa ser maior que 0\n')
    else:    
        print("ERRO: Histórico de depósitos não é uma lista válida!")
    

def sacar(historico_saques, valor, saldo_total, saques_realizados):
    if isinstance(historico_saques, list):  # Verifica se é uma lista
        if saques_realizados >= LIMITE_SAQUES:
            print(" Você já atingiu o limite de 3 saques diários! Tente novamente amanhã.")
            return saldo_total, saques_realizados

        if valor > 500:
            print(' Esse valor ultrapassou seu limite de R$500 por saque. Tente um valor menor.')
            return saldo_total, saques_realizados

        if valor <= saldo_total:
            saldo_total -= valor  
            historico_saques.append(valor)  # <<-- historicos das transaçoes de saque
            saques_realizados += 1  
            print(" Saque realizado com sucesso!")
            print('-' * 50)
            print(f" Seu saldo atual é R$:{saldo_total}")
            print('-' * 50)
            print(f" Você ainda pode realizar {LIMITE_SAQUES - saques_realizados} saques hoje.")           
            return saldo_total
        
        else:
            print('-' * 50)
            print(f" Saldo insuficiente! Seu saldo atual é R$:{saldo_total}. Tente um valor menor.")
            print('-' * 50)
            return saldo_total


def extrato(historico_depositos, historico_saques, saldo_total):
    
    print(' Depósitos Realizados:')
    if historico_depositos:
        for i, deposito in enumerate(historico_depositos, 1): # numerando cada deposito
            print(f' {i}º depósito: R$:{deposito}')
    else:
        print(' Nenhum depósito realizado.')

    print('\n Saques Realizados:')
    if historico_saques:
        for i, saque in enumerate(historico_saques, 1): # numerando cada saque
            print(f' {i}º saque: R$:{saque}')
    else:
        print(' Nenhum saque realizado.')
        return historico_depositos, historico_saques, saldo_total
    print('=' * 50)
    print(f'Saldo Atual: R$:{saldo_total}\n'.center(50)) 
    print('¨' * 50)


def criar_usuario(usuarios):
    if isinstance(usuarios, list):  # Verifica se é uma lista
        #while True:
            #cpf = str(input('Informe seu CPF (somente número): ')).strip()
            #validador = CPF()
            #if validador.validate(cpf):  # Verifica se o CPF é válido 
            #    print("CPF válido!")
            #    break  # Sai do loop se o CPF for válido
            #else:
            #    print("CPF inválido! Por favor, tente novamente.")
        usuario = filtrar_usuario(cpf, usuarios)

        if usuario:
            print("        Atenção \nJá existe usuário com esse CPF! ")
            return
        # Cadastrando dados do Usuário
        nome = str(input('Digite seu nome: '))
        sobrenome = str(input('Sobrenome: '))
        nascimento = str(input('Digite sua Data de nascimento: (DIA/MÊS/ANO) '))
        cep = str(input("Digite seu CEP: ")) 
        estado = str(input("Digite seu Estado: ")).upper()
        cidade = str(input("Digite a Cidade: ")).upper()
        bairro = str(input("Bairro: ")).upper()
        rua = str(input("Rua: ")).upper()
        num_rua = str(input("Digite o número: "))
        complemento = str(input('Complemento: '))

        # Armazenando os dados do usuário
        usuarios.append({"nome": nome, "sobrenome": sobrenome,
                         "nascimento": nascimento, "cpf": cpf, 
                         "cep": cep, "num_rua": num_rua,
                         "complemento": complemento, "cidade": cidade,
                         "estado": estado, "bairro": bairro, "rua": rua})
        print("#" * 30)
        print("Usuário Criado com Sucesso!")
        print('#' * 30)


def filtrar_usuario(cpf, usuarios):
        usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf] # verificando se ja tem cpf. 
        return usuarios_filtrados[0] if usuarios_filtrados else None    


def criar_conta(agencia, numero_conta, usuarios):
    cpf = str(input("informe o CPF do usuário: ")).strip()
    usuario = filtrar_usuario(cpf, usuarios) # filtrando o usuario pelo cpf para saber se ja tem conta.

    if usuario:
        print("#" * 30)
        print("Conta Criada com sucesso!")
        print("#" * 30)
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
    print("\n ¬¬ Usuário não encontrado, Fluxo de Criação de conta encerrado! ¬¬")


def listar_conta(contas):
    for conta in contas:
        linha = f'''\
            Agência:\t{conta['agencia']}
            C/c:\t\t{conta["numero_conta"]}
            Titular:\t{conta['usuario']['nome']}
        '''
        print(textwrap.dedent(linha))

# Programa principal
def main(): 
    while True:
        acao = menu(['Depósito', 'Saque', 'Extrato', 'Criar Usuário', 'Cria Conta', 'Listar Conta', 'Sair'])

        # Depositando valor
        if acao == 1 :
            print(linha())
            print('DEPÓSITO')
            print('=' * 50)
            valor = int(input('Qual valor deseja depositar? R$: '))
            saldo_total = deposito(historico_depositos, valor) # Atualizando Saldo

        # Sacando Valor
        elif acao == 2 : 
            print('-' * 50)
            print(f'SAQUE \nSeu saldo Atual é R$:{saldo_total}'.center(50))
            print('=' * 50)
            valor = int(input("Qual valor você quer sacar? R$: "))
            saldo_total = sacar(historico_saques, valor, saldo_total, saques_realizados) # Atualizando Saldo

        #  Vendo Extrato
        elif acao == 3 :
            print(linha())
            print('\n EXTRATO BANCÁRIO '.center(50))
            print('=' * 50)
            extrato(historico_depositos, historico_saques, saldo_total) 

        #  Criando da usuário
        elif acao == 4 :
            print(linha())
            print('\n Criando Usuário '.center(50))
            print('=' * 50)
            criar_usuario(usuarios)


        #  Criando da conta
        elif acao == 5 :
            print(linha())
            print('\n Criar Conta '.center(50))
            print('=' * 50)
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)
            if conta:
                contas.append(conta)
            

        elif acao == 6 :
            print(linha())
            print('\n Listagem de Conta '.center(50))
            print('=' * 50)
            listar_conta(contas)   


        #  Saindo da conta
        elif acao == 7 :
            print('Encerrando sua sessão...')
            for c in range(3, 0, -1):
                sleep(1)
                print(c)
            break
        else:
            print(' Opção inválida! Tente novamente.')

main()
print('\nObrigado por usar o BANCO SUZANO! Volte sempre!')
