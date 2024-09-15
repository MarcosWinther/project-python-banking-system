# 👨‍💻 Sistema Bancário em Python

Este projeto é um sistema bancário que permite a criação de clientes, contas, e a realização de transações como depósito, saque e consulta de extrato. O sistema foi projetado utilizando conceitos de orientação a objetos como herança, polimorfismo e classes abstratas.

### Sobre esse Projeto:

O desafio desse projeto foi proposto no curso ``Criando um Sistema Bancário com Python`` ministrado pelo expert [Guilherme Carvalho](https://www.linkedin.com/in/decarvalhogui/) na trilha de Python do Bootcamp "[NTT DATA](https://www.linkedin.com/company/nttdata/posts/?feedView=all) - Engenharia de Dados com Python" disponível na plataforma da [DIO](https://www.dio.me/).


## 💻 Tecnologia utilizada no projeto:
<div>
   <img alt="Python" src="https://img.shields.io/badge/Python-14354C?style=for-the-badge&logo=python&logoColor=white">
</div>


## 🛠 Funcionalidades

- **Depósito:** O cliente pode adicionar fundos à sua conta.
- **Saque:** O cliente pode sacar dinheiro, respeitando o saldo disponível e o limite de saques diários.
- **Extrato:** Exibe todas as transações realizadas na conta e o saldo atual.
- **Cadastro de Cliente:** Permite cadastrar novos clientes no sistema.
- **Criação de Conta:** Permite criar uma nova conta para clientes existentes.
- **Listar Contas:** Exibe todas as contas cadastradas no banco.
- **Sair:** Encerra o programa.


## ⚠ Regras do Sistema

- **Depósito:** O valor deve ser positivo.
- **Saque:** 
  - O valor deve ser menor ou igual ao saldo disponível.
  - O número máximo de saques diários é 3.
  - O valor máximo permitido por saque é de R$500,00.
- **Extrato:** Exibe todas as transações da conta (saques e depósitos) e o saldo atual.


## 🔨 Melhorias Implementadas

- **Orientação a Objetos (OO):** A estrutura foi refatorada utilizando classes como `Cliente`, `Conta`, e `Transacao`.
- **Classes Abstratas:** A classe `Transacao` foi criada como abstrata para definir uma interface para as transações de depósito e saque.
- **Herança:** As classes `PessoaFisica` herda de `Cliente` e `ContaCorrente` herda de `Conta`.
- **Histórico de Transações:** O sistema agora registra todas as transações (saques e depósitos) associadas a uma conta.
- **Validação de CPF:** As transações agora validam o CPF do cliente antes de serem realizadas.
  

## 📂 Estrutura do Código

- **Cliente:** Classe base para representar clientes, contendo o endereço e uma lista de contas.
- **PessoaFisica:** Subclasse de `Cliente`, com atributos como nome, CPF e data de nascimento.
- **Conta:** Classe base que contém o saldo, número da conta, agência e um histórico de transações.
- **ContaCorrente:** Subclasse de `Conta`, com limites de saque e número máximo de saques diários.
- **Transacao (Abstrata):** Define uma interface para transações financeiras como saque e depósito.
- **Saque e Deposito:** Implementam as transações financeiras que são registradas no histórico da conta.
- **Historico:** Classe que registra todas as transações realizadas por uma conta.


## 👨‍🔧 Como Executar

1. Clone o repositório ou baixe os arquivos do projeto.
2. Abra o terminal e navegue até o diretório onde o arquivo está localizado.
3. Execute o arquivo Python com o seguinte comando:

    ```bash
    python nome_do_arquivo.py
    ```

4. Siga as instruções no terminal para interagir com o sistema.


## ✅ Exemplo de Uso

Ao executar o programa, você verá o seguinte menu:

````sh
============== MENU ==============
[d]  Depositar
[s]  Sacar
[e]  Extrato
[nc] Nova conta
[lc] Listar contas
[nu] Novo cliente
[q]  Sair

=>
````

Você pode escolher a operação desejada digitando a letra correspondente.


## 🤝 Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues e pull requests.

## 👨‍💻 Expert

<p>
    <img 
      align=left 
      margin=10 
      width=80 
      src="https://avatars.githubusercontent.com/u/44624583?v=4"
    />
    <p>&nbsp&nbsp&nbspMarcos Winther<br>
    &nbsp&nbsp&nbsp
    <a href="https://github.com/MarcosWinther">
    GitHub</a>&nbsp;|&nbsp;
    <a href="https://www.linkedin.com/in/marcoswinthersilva/">LinkedIn</a>
    </p>
</p>
<br/><br/>

---

⌨️ com 💜 por [Marcos Winther](https://github.com/MarcosWinther)
