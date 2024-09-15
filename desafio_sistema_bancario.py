from abc import ABC, abstractmethod
from datetime import datetime
import textwrap

class Cliente:
    def __init__(self, endereco):
        self.endereco = endereco
        self.contas = []

    def realizar_transacao(self, conta, transacao):
        transacao.registrar(conta)

    def adicionar_conta(self, conta):
        self.contas.append(conta)

class PessoaFisica(Cliente):
    def __init__(self, nome, data_nascimento, cpf, endereco):
        super().__init__(endereco)
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.cpf = cpf

class Conta:
    def __init__(self, numero, cliente):
        self._saldo = 0
        self._numero = numero
        self._nro_agencia = "0001"
        self._cliente = cliente
        self._historico = Historico()
    
    @classmethod
    def nova_conta(cls, cliente, numero):
        return cls(numero, cliente)
    
    @property
    def saldo(self):
        return self._saldo
    
    @property
    def numero(self):
        return self._numero
    
    @property
    def nro_agencia(self):
        return self._nro_agencia
    
    @property
    def cliente(self):
        return self._cliente
    
    @property
    def historico(self):
        return self._historico
    
    def sacar(self, valor):
        saldo = self.saldo
        excedeu_saldo_conta = valor > saldo

        if excedeu_saldo_conta:
            print("\n*** Saldo insuficiente para essa transação! ***")

        elif valor > 0:
            self._saldo -= valor
            print("\n### Saque realizado com sucesso! ###")
            return True
        
        else:
            print("\n*** Valor inválido! Verifique o valor do saque e tente novamente! ***")
        
        return False
    
    def depositar(self, valor):
        saldo = self.saldo

        if valor > 0:
            self._saldo += valor
            print("\n### Depósito realizado com sucesso! ###")
        
        else:
            print("\n*** Valor inválido! Verifique o valor do depósito e tente novamente! ***")
            return False

        return True

class ContaCorrente(Conta):
    def __init__(self, numero, cliente, limite=500, limite_saques=3):
        super().__init__(numero, cliente)
        self.limite = limite
        self.limite_saques = limite_saques

    def sacar(self, valor):
        numero_saques = len(
            [transacao for transacao in self.historico.transacoes if transacao["tipo"] == Saque.__name__]
        )

        limite_excedeu = valor > self.saldo
        excedeu_saques = numero_saques >= self.limite_saques

        if limite_excedeu:
            print("\n*** Transação não realizada! Valor solicitado é maior que o limite permitido! ***")

        elif excedeu_saques:
            print("\n*** Transação não realizada! Limite diário excedido! ***")

        else:
            return super().sacar(valor)

        return False
    
    def __str__(self):
        return f"""\
            Agência:\t{self.nro_agencia}
            Número Conta Corrente:\t{self.numero}
            Titular da Conta:\t{self.cliente.nome}
        """

class Historico:
    def __init__(self):
        self._transacoes = []
    
    @property
    def transacoes(self):
        return self._transacoes
    
    def adicionar_transacao(self, transacao):
        self._transacoes.append(
            {
                "tipo": transacao.__class__.__name__,
                "valor": transacao.valor,
                "data": datetime.now().strftime("%d-%m-%Y %H:%M:%S")
            }
        )

class Transacao(ABC):
    @property
    @abstractmethod
    def valor(self):
        pass

    @abstractmethod
    def registrar(self, conta):
        pass

class Saque(Transacao):
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor

    def registrar(self, conta):
        sucesso_transacao = conta.sacar(self.valor)

        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)

class Deposito(Transacao):
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor

    def registrar(self, conta):
        sucesso_transacao = conta.depositar(self.valor)

        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)



def menu():
    menu = '''\n
    ============== MENU ==============
    [d]\tDepositar
    [s]\tSacar
    [e]\tExtrato
    [nc]\tNova conta
    [lc]\tListar contas
    [nu]\tNovo cliente
    [q]\tSair
    => '''
    return input(textwrap.dedent(menu))

def filtrar_cliente(cpf, clientes):
    clientes_filtrados = [cliente for cliente in clientes if cliente.cpf == cpf]
    return clientes_filtrados[0] if clientes_filtrados else None

def verificar_conta_cliente(cliente):
    if not cliente.contas:
        print("*** \nCliente não possui contas em nosso Banco! ***")
        return
    
    return cliente.contas[0]
    
def depositar(clientes):
    cpf = input("Informe o CPF do Titular da Conta: ")
    cliente = filtrar_cliente(cpf, clientes)

    if not cliente:
        print("*** Cliente não cadastrado em nosso sistema! \nPor gentileza solicite a abertura de conta! ***")
        return
    
    valor = float(input("Digite o valor do depósito: R$"))
    transacao = Deposito(valor)

    conta = verificar_conta_cliente(cliente)

    if not conta:
        return
    
    cliente.realizar_transacao(conta, transacao)

def sacar(clientes):
    cpf = input("Informe o CPF do Titular da Conta: ")
    cliente = filtrar_cliente(cpf, clientes)

    if not cliente:
        print("*** Cliente não cadastrado em nosso sistema! \nPor gentileza solicite a abertura de conta! ***")
        return
    
    valor = float(input("Digite o valor do saque: R$"))
    transacao = Saque(valor)

    conta = verificar_conta_cliente(cliente)

    if not conta:
        return
    
    cliente.realizar_transacao(conta, transacao)
    

def exibir_extrato_bancario(clientes):
    cpf = input("Informe o CPF do Titular da Conta: ")
    cliente = filtrar_cliente(cpf, clientes)

    if not cliente:
        print("*** Cliente não cadastrado em nosso sistema! \nPor gentileza solicite a abertura de conta! ***")
        return
    
    conta = verificar_conta_cliente(cliente)

    if not conta:
        return
    
    print("\n======= EXTRATO BANCÁRIO =======")
    transacoes = conta.historico.transacoes

    extrato = ""

    if not transacoes:
        extrato = "Não foram encontrados movimentações bancárias na Conta do Titular!"
    else:
        for transacao in transacoes:
            extrato += f"\n{transacao['tipo']}:\n\tR${transacao['valor']:.2f}"

    print(extrato)
    print(f"\nSaldo:\n\tR${conta.saldo:.2f}")
    print("====================================")

def criar_cliente(clientes):
    cpf = input("Informe o CPF para o cadastro (somente número): ")
    cliente = filtrar_cliente(cpf, clientes)

    if cliente:
        print("*** Cliente já cadastrado no nosso sistema! ***")
        return
    
    
    nome = input("Digite seu nome completo: ")
    data_nascimento = input("Digite sua data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe seu endereco (Logradouro, n° - bairro - cidade/sigla do Estado): ")

    cliente = PessoaFisica(nome=nome, data_nascimento=data_nascimento, cpf=cpf, endereco=endereco)

    clientes.append(cliente)

    print("*** Cliente cadastrado com sucesso! Seja bem-vindo(a)! ***")

def criar_conta(numero_conta, clientes, contas):
    cpf = input("Informe o CPF do Titular para a criação da conta: ")
    cliente = filtrar_cliente(cpf, clientes)

    if not cliente:
        print("\n*** Cliente não cadastrado em nosso sistema! \nCriação de conta cancelada! ***")
        return

    conta = ContaCorrente.nova_conta(cliente=cliente, numero=numero_conta)
    contas.append(conta)
    cliente.contas.append(conta)

    print("\n### Conta criada com sucesso! \nSeja-vindo(a) ao nosso Banco! ###")

def listar_contas_cliente(contas):
    for conta in contas:
        print("=" * 100)
        print(textwrap.dedent(str(conta)))

def main():
    clientes = []
    contas = []

    while True:
        
        opcao = menu()

        if opcao == 'd':
            depositar(clientes)
                
        elif opcao == 's':
            sacar(clientes)
            
        elif opcao == 'e':
            exibir_extrato_bancario(clientes)

        elif opcao == 'q':
            break

        elif opcao == 'nu':
            criar_cliente(clientes)

        elif opcao == 'nc':
            numero_conta = len(contas) + 1
            criar_conta(numero_conta, clientes, contas)
        
        elif opcao == 'lc':
            listar_contas_cliente(contas)
        else:
            print("*** Opcão inválida! Selecione a opção correta e tente novamente! ***")

main()



