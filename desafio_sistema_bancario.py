import textwrap

def menu():
    menu = '''\n
    ============== MENU ==============
    [d]\tDepositar
    [s]\tSacar
    [e]\tExtrato
    [nc]\tNova conta
    [lc]\tListar contas
    [nu]\tNovo usuário
    [q]\tSair
    => '''
    return input(textwrap.dedent(menu))

def depositar(saldo, valor, extrato, /):
    
    if(valor > 0):
        saldo += valor
        extrato = f"Valor depositado: R${saldo:.2f}"
        return saldo, print(extrato)
    
    extrato = "Depósito não realizado! Verifique o valor e tente novamente"

    return saldo, print(extrato)

def verificar_limite_saque(numero_saque, limite_qtd_saque):
    
    if(numero_saque >= limite_qtd_saque):
        return True
    
    return False

def verificar_valor_limite(valor_saque, valor_limite):

    if valor_saque >= valor_limite:
        return True
    
    return False

def sacar(*, saldo, valor, qtd_saque, limite_qtd_saque, limite_saque, extrato):

    quantidade_saque_excedeu = verificar_limite_saque(qtd_saque, limite_qtd_saque)
    extrato = "Transação não realizada"

    if quantidade_saque_excedeu:
        extrato = "Você ultrapassou a quantidade de saques disponíveis!"

    elif valor > 0 and valor <= saldo:
        valor_limite_excedeu = verificar_valor_limite(valor, limite_saque)

        if valor_limite_excedeu:
            extrato = "Você ultrapassou o valor do limite permitido para saque!"

        else:
            saldo -= valor
            qtd_saque += 1
            print(qtd_saque)
            extrato = f"Saque realizado com sucesso! Valor do saque R${valor:.2f}\nSaldo atual: R${saldo:.2f}"

    elif valor > saldo or saldo == 0:
        extrato = "Saldo insufiente para essa transação"

    else:
        extrato = "Valor inválido! Verifique o valor e tente novamente"
    
    return qtd_saque, saldo, print(extrato)

def exibir_extrato_bancario(extrato, /, *, saldo):
    print("============= EXTRATO =============")
    extrato = f"O saldo da conta: R${saldo:.2f}"
    return saldo, print(extrato)

def criar_usuario(usuarios):
    cpf = input("Informe seu CPF (somente números): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n### Atenção: Usuário com esse CPF já cadastrado em novo sistema! ###")
        return
    
    nome = input("Digite seu nome completo: ")
    data_nascimento = input("Digite sua data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe seu endereco (Logradouro, n° - bairro - cidade/sigla do Estado): ")

    usuarios.append = ({"nome": nome, "cpf": cpf, "data_nascimento": data_nascimento, "endereco": endereco})

    print("*** Usuário criado com sucesso ***")

def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta_corrente(agencia, numero_conta, usuarios):
    cpf = input("Informe o seu CPF: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("*** Sua conta foi criada com sucesso! ***")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
    
    print("### Usuário não encontrado! POr favor, realize seu cadastro! ###")

def main():
    LIMITES_SAQUES = 3
    NUMERO_AGENCIA = "0001"

    saldo_conta = 0
    valor_limite_saque = 500
    extrato = ''
    numero_saques = 0
    
    usuarios = []
    contas = []

    while True:
        
        opcao = menu()

        if opcao == 'd':

            valor_deposito = float(input('Informe o valor do depósito: R$'))

            saldo_conta, extrato = depositar(saldo_conta, valor_deposito, extrato)
                
        elif opcao == 's':
            
            valor_saque = float(input('Informe o valor do saque: R$'))

            numero_saques, saldo_conta, extrato = sacar(
                saldo=saldo_conta, 
                valor=valor_saque, 
                qtd_saque=numero_saques, 
                limite_qtd_saque=LIMITES_SAQUES, 
                limite_saque=valor_limite_saque, 
                extrato=extrato
            )
            
        elif opcao == 'e':
            extrato, saldo_conta = exibir_extrato_bancario(extrato, saldo=saldo_conta)

        elif opcao == 'q':
            break

        elif opcao == 'nu':
            criar_usuario(usuarios)

        elif opcao == 'nc':
            numero_conta = len(contas) + 1
            conta = criar_conta_corrente(NUMERO_AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)
        
        else:
            print("Opcão inválida! Tente novamente!")

main()



