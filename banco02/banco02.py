menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[nc] Nova Conta
[lc] Listar Contas
[nu] Novo Usuário
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3
AGENCIA = '0001'
usuarios = []
contas = []


#criando a função depositar:
def depositar(valor_deposito, saldo, extrato, /):
    if valor_deposito > 0:
        saldo += valor_deposito
        extrato += f'Depósito: R$ {valor_deposito:.2f}\n'
        print("\n Depósito realizado com sucesso!")
    else:
        print("\n Operação falhou! O valor informado é inválido!")

    return saldo, extrato

#criando a função sacar:
def sacar (*, valor_saque,saldo, extrato, limite, numero_saques, LIMITE_SAQUES):
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
        print("\n Saque realizado com sucesso!")
    return extrato, saldo, numero_saques
#criando a função exibir_extrato:
def exibir_extrato(saldo, extrato):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo:\t\tR$ {saldo:.2f}")
    print("========================================")
#criando a função criar_usuario
def criar_usuario(usuarios):
    cpf = input("Informe o CPF (somente número): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n Já existe usuário com esse CPF!")
        return

    nome = input("Informe o seu nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})

    print("Usuário criado com sucesso!")
#criando a função filtrar_usuario:
def filtrar_usuario(cpf, usuarios):
    for usuario in usuarios:
        if usuario["cpf"] == cpf:
            return usuario
    return None
#criar a função criar_conta:
def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = None
    for u in usuarios:
        if u["cpf"] == cpf:
            usuario = u
            break
    if usuario:
        print("\nConta criada com sucesso!")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
    
    print("\n Usuário não encontrado, fluxo de criação de conta encerrado! ")
    return None
#criar a função listar_contas:
def listar_contas(contas):
    print("\n================ LISTA DE CONTAS ================")
    if not contas:
        print("Não há contas cadastradas.")
    else:
        for conta in contas:
            print(f"Agência:\t{conta['agencia']}")
            print(f"C/C:\t\t{conta['numero_conta']}")
            print(f"Titular:\t{conta['usuario']['nome']}")
            print("--------------------------------------------------")

while True:

    opcao = input(menu)

    if opcao == "d":
        valor_deposito = float(input("VALOR DE DEPÓSITO: "))
        saldo, extrato = depositar(valor_deposito, saldo, extrato)

    elif opcao == "s":
        valor_saque = float(input('VALOR SAQUE: '))
        extrato, saldo, numero_saques = sacar (valor_saque =valor_saque,saldo=saldo, extrato=extrato, limite=limite, numero_saques=numero_saques, LIMITE_SAQUES=LIMITE_SAQUES)

    elif opcao == "e":
        exibir_extrato(saldo, extrato)

    elif opcao == "nu":
            criar_usuario(usuarios)

    elif opcao == "nc":
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)
    
    elif opcao == "lc":
        listar_contas(contas)

    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")

