# Variables:

menu = """

=================
[d] Depositar
[s] Sacar
[e] Extrato
[nu] Novo usuario
[nc] Nova conta
[lc] Listar contas
[q] Sair
=================

=>"""

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3
LIMITE_TRANSACOES = 10
usuarios = []
NUMERO_AGENCIA = "0001"
contas = []

# --------------------------------------------------------------------------------------------------------------
# Functions:

def check_numero(num):
    if num.isnumeric():
        return float(num)

def deposito(saldo, valor_deposito, extrato):    

    if valor_deposito is None:
        print("Insira um valor numérico positvo.")
    else:        
        if valor_deposito > 0:
            saldo += valor_deposito
            extrato = extrato + f"\n+ R${valor_deposito:.2f}"
            print(f"Depósito realizado. Saldo atual: R${saldo:.2f}")
        else:
            print("Valor de depósito inválido. Insira um valor numerico positivo.")

    return saldo, extrato 
    
def saque(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    sem_saldo = valor > saldo
    sem_limite = valor > limite
    sem_saques = numero_saques >= limite_saques

    if sem_saldo:
        print("Sem saldo.")
    elif sem_limite:
        print("Limite excedido.")
    elif sem_saques:
        print("Sem saques.")
    else:
        if valor > 0:
            saldo -= valor
            extrato = extrato + f"\n- R${valor_saque:.2f}"
            numero_saques += 1
            print(f"Saque realizado. Saldo atual: R${saldo:.2f}")
        else:
            print("Insira um valor numero positivo")
    
    return saldo, extrato, numero_saques
    
def ver_extrato(saldo,/,*, extrato):
    print("Extrato:\n--------------------------")
    if extrato:
            print(f"{extrato}\nSaldo: R${saldo:.2f}")
    else:
        print(f"Sem movimentações.\nSaldo: R${saldo:.2f}")

def criar_usuario(usuarios, cpf):

    if cpf is None:
        print("Insira um valor numérico positvo.")
    else:
        usuario_existe = False
        for u in usuarios:
            if u["cpf"] == cpf:
                usuario_existe = True

        if usuario_existe:
            print("Usuario ja cadastrado.")
        else:
            nome = input("Insira nome: ")
            data_nasc = input("Insira a data de nascimento (dd-mm-aaa): ")
            endereco = input("Insira endereco (logradouro, numero, bairro, cidade, sigla estado): ")

            usuarios.append({"nome": nome, "data_nascimento" : data_nasc, "cpf" : cpf, "endereco" : endereco})
            print("Usuario registrado.")

def criar_conta(cpf, agencia, contas, usuarios):

    if cpf is None:
        print("Insira um valor numérico positvo.")
    else:
        usuario_existe = False
        for u in usuarios:
            if u["cpf"] == cpf:
                usuario_existe = True

        if usuario_existe == False:
            print("Usuario inexistente.")
        else:            
            user_nome = ""
            for u in usuarios:
                if u["cpf"] == cpf:
                    user_nome = u["nome"]
            
            numero_conta = agencia + " - " + str(len(contas) + 1) + " - " + user_nome
            contas.append(numero_conta)

        print("Contas cadastradas: ")
        mostrar_contas(contas)

        return contas

def mostrar_contas(contas):

    if len(contas) == 0:
        print("Nenhuma conta cadastrada.")
    else:
        print("Contas cadastradas: ")
        for c in contas:
            print("\n" + c)

# --------------------------------------------------------------------------------------------------------------
# Main program:

while True:

    opcao = input(menu)

    if opcao == "d": # deposito

        valor_deposito = input("Valor do depósito R$: ")
        valor_deposito = check_numero(valor_deposito)

        saldo, extrato = deposito(saldo, valor_deposito, extrato)

    elif opcao == "s": # saque

        valor_saque = input("Valor do saque R$: ")
        valor_saque = check_numero(valor_saque)

        saldo, extrato, numero_saques = saque(saldo=saldo,
                                                valor=valor_saque,
                                                extrato=extrato,
                                                limite=limite,
                                                numero_saques=numero_saques,
                                                limite_saques=LIMITE_SAQUES
                                                )

    elif opcao == "e": # extrato
        ver_extrato(saldo, extrato=extrato)

    elif opcao == "nu": # novo usuario

        cpf = input("Inserir CPF (somente numeros): ")
        cpf = check_numero(cpf)
        criar_usuario(usuarios, cpf)

    elif opcao == "nc": # nova conta

        cpf = check_numero(input("Inserir CPF (somente numeros): "))

        contas = criar_conta(cpf, NUMERO_AGENCIA, contas, usuarios)

    elif opcao == "lc":

        mostrar_contas(contas)

    elif opcao == "q": # sair

        break

    else:

        print("Operação inválida, por favor selecione novamente a operação desejada.")