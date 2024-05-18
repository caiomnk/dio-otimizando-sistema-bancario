import textwrap

def menu():
    menu = """\n
    =============== BANCO BANQUITO ==============
    Olá cliente!
    => Selecione a operação desejada:

    [0]\tDepositar
    [1]\tSacar
    [2]\tExtrato
    [3]\tNovo Cliente
    [4]\tCriar Conta
    [5]\tListar Contas
    [6]\tSair
    =============================================
    => """
    return input(textwrap.dedent(menu))

def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor 
        extrato += f"Depósito:\tR$ {valor:.2f}\n"
        print("\n Depósito concluído! ")
    else:
        print("\n!!!! Erro na operação! O valor declarado não e válido. !!!")
    
    return saldo, extrato 

def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):

    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limite_saques

    if excedeu_saldo:
        print("\n!!!! Operação inválida! Sem saldo suficiente em sua conta. !!!")

    elif excedeu_limite:
        print("\n!!! Operação inválida! Valor informado de saque excedeu o limite em conta. !!!")

    elif excedeu_saques:
        print("\n!!! Operação inválida! Limite de saques diários atingidos (3). !!!")

    elif valor > 0:
        saldo -= valor 
        extrato += f"Saque:\t\tR$ {valor:.2f}\n"
        numero_saques += 1
        print("\n Saque realizado com sucesso! ")

    else:
        print("\n!!!! Operação inválida! O valor informado não e válido. ")
    return saldo, extrato

def exibir_extrato(saldo, /, *, extrato):
    print("\n##########  EXTRATO BANCÁRIO  ##########")
    print("Não foram realizadas movimentações recentes nessa conta." if not extrato else extrato)
    print(f"\nSaldo:\t\tR$ {saldo:.2f}")
    print("##########################################")

def criar_usuario(usuarios):
    cpf = input("Informe o CPF do titular da conta (somente números): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n!!!! Usuário já cadsatrado com o CPF informado !!!!")
        return
    
    nome = input("Favor informar nome completo: ")
    data_nascimento = input("Informe data de nascimento (dd/mm/aaaa): ")
    endereco = input("Informe seu endereço (Logradouro, número-bairro-cidade/UF): ")
    cep = input("Informe seu cep (somente números): ")

    usuarios.append({"nome": nome, "data de nascimento": data_nascimento, "cpf": cpf, "endereco": endereco, "cep": cep,})

    print("#### Usuário criado com sucesso! ####")

def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario ["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do cliente da conta (somente números): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n#### Conta criada com sucesso junto ao banco! ####")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}

    print("\n!!!! Usuário não encontrado na base de dados, encerrando processo de cadastro! ####")

def listar_contas(contas):
    for conta in contas:
        linha = f"""\
            Agência:\t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
        """
        print("=" * 100)
        print(textwrap.dedent(linha))

def sair(sair):
    print("\n########## Até logo! Obrigado por ser nosso cliente! ##########")


def main(): 
    LIMITE_SAQUES = 3
    AGENCIA = "0001"

    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []

    while True:
        opcao = menu()

        if opcao == "0":
            valor = float(input("Informe o valor do depósito: "))

            saldo, extrato = depositar(saldo, valor, extrato)

        elif opcao == "1":
            valor = float(input("Infome o valor do saque: "))

            saldo, extrato = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                limite_saques=LIMITE_SAQUES, 
            )
        
        elif opcao == "2":
            exibir_extrato(saldo, extrato=extrato)
       
        elif opcao == "3":
            criar_usuario(usuarios)

        elif opcao == "4":
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)

        elif opcao == "5":
            listar_contas(contas)

        elif opcao == "6":
            sair(sair)
            break

        
        else:
            print("Opção inválida, favor escolher uma das opções válidas no menu inicial.")

main()





