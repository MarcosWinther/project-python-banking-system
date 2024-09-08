def exibir_saldo_conta(saldo):
     print("============= EXTRATO =============")
     return print(f"O saldo da conta: R${saldo:.2f}")

#--------------------------------------

menu = """
DIGITE A OPÇÃO DESEJADA:

[d] - Depositar
[s] - Sacar
[e] - Extrato Bancário
[q] - Sair

=> """

saldo_conta = 0
valor_limite_saque = 500
numero_saques = 0
LIMITES_SAQUES = 3

while True:
    
    opcao = input(menu)

    if opcao == "d":
        valor_deposito = float(input("Informe o valor do depósito: R$"))
        
        if valor_deposito > 0:
             saldo_conta += valor_deposito
             print("Depósito realizado com sucesso!")
             exibir_saldo_conta(saldo=saldo_conta)

        else:
            print("Depósito não realizado! verifique o valor e tente novamente!")
            
    elif opcao == "s":
        
        valor_saque = float(input("Informe o valor do saque: R$"))

        excedeu_qtd_saques = numero_saques >= LIMITES_SAQUES

        excedeu_valor_limite = valor_saque >= valor_limite_saque

        if excedeu_qtd_saques:
            print("Transação não realizada! Você ultrapassou a quantidade de saques disponíveis!")
        
        elif (valor_saque > 0) and (valor_saque <= saldo_conta):
            if excedeu_valor_limite:
                print("Transação não realizada! Você ultrapassou o valor do limite permitido para saque!")

            else:
                numero_saques += 1
                saldo_conta -= valor_saque
                exibir_saldo_conta(saldo=saldo_conta)
        
        elif saldo_conta == 0:
            print("Saldo insuficiente para essa transação!")

        else:
            print("Valor inválido! Verifique o valor e tente novamente!")
        
    elif opcao == "e":
        exibir_saldo_conta(saldo=saldo_conta)

    elif opcao == "q":
        break

    else:
        print("Operação inválida! Por favor selecionar novamente a operação desejada com a opção correta!")