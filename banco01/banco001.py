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

while True:

    opcao = input(menu)

    if opcao == "d":
        valor_deposito = float(input("VALOR DE DEPÓSITO: "))
        if valor_deposito > 0:
            saldo += valor_deposito
            extrato += f'Depósito: R$ {valor_deposito:.2f}\n'

    elif opcao == "s":
        valor_saque = float(input('VALOR SAQUE: '))
        if numero_saques >= LIMITE_SAQUES:
            print('Já foram realizados as quantidade limite diária de saques.')
        elif valor_saque > saldo:
            print('Saldo insuficiente.')
        elif valor_saque > limite:
            print('O valor desejado excede o limite.')
        elif valor_saque <= saldo:
            saldo -= valor_saque
            numero_saques += 1
            extrato += f'Saque: R$ {valor_saque:.2f}\n'

    elif opcao == "e":
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")

    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")