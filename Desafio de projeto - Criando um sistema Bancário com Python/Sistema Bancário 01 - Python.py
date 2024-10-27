menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3
movimentacoes = []

def depositar(saldo):
    print("""Valor do Depósito
    => """)
    deposito = float(input())
    if deposito > 0:
        saldo += deposito
        print(f"O depósito no valor de R$ {deposito:.2f} foi realizado com sucesso!")
        movimentacoes.append(deposito)

    else:
        print("Esse valor é inválido")

    return saldo

def sacar(saldo, numero_saques, limite):
    print("""Valor do Saque
    => """)
    saque = float(input())
    if numero_saques >= LIMITE_SAQUES:
        print("você atingiu o limite diário, volte novamente amanhã!")
    elif saque <= 0:
        print("valor inválido")
    elif saque > saldo:
        print("saldo insuficiente.")
    elif saque > limite:
        print(f"o valor não pode ser superior à R$ {limite:.2f}")
    else:
        saldo -= saque
        print(f"O saque no valor de R$ {saque:.2f} foi realizado com sucesso!")
        movimentacoes.append(saque * -1)
        numero_saques += 1  
          
    return saldo, numero_saques


while True:
    opcao = input(menu)

    if opcao == "d":
        saldo = depositar(saldo)
        
    elif opcao == "s":
        saldo, numero_saques = sacar(saldo, numero_saques, limite)

    elif opcao == "e":
        print("Extrato".center(20,"-"))
        for movimentacao in movimentacoes:
            if movimentacao > 0:
                print(f"depósito.....R$ {movimentacao}", end="\n")
            if movimentacao < 0:
                movimentacao *= -1
                print(f"saque........R$ {movimentacao}", end="\n")
        print(f"\n Saldo Final: R$ {saldo:.2f}")

    elif opcao == "q":
        break

    else:
        print("Operação Inválida, por favor selecione novamente a operação desejada")