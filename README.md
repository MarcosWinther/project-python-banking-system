# 👨‍💻 Sistema Bancário em Python

Este projeto é um sistema bancário simples, implementado em Python, que permite ao usuário realizar operações básicas como depósito, saque e consulta de saldo.

O desafio desse projeto foi proposto no curso ``Criando um Sistema Bancário com Python`` ministrado pelo expert [Guilherme Carvalho](https://www.linkedin.com/in/decarvalhogui/) na trilha de Python do Bootcamp "[NTT DATA](https://www.linkedin.com/company/nttdata/posts/?feedView=all) - Engenharia de Dados com Python" disponível na plataforma da [DIO](https://www.dio.me/).


## 💻 Tecnologia utilizada no projeto:
<div>
   <img alt="Python" src="https://img.shields.io/badge/Python-14354C?style=for-the-badge&logo=python&logoColor=white">
</div>


## 🛠 Funcionalidades

- **Depósito:** O usuário pode adicionar fundos à sua conta.
- **Saque:** O usuário pode sacar dinheiro da sua conta, respeitando o limite de saques diários e o valor máximo permitido por saque.
- **Extrato:** O usuário pode visualizar o saldo atual da conta.
- **Sair:** O usuário pode encerrar o programa.


## ⚠ Regras do Sistema

- **Depósito:** O valor deve ser positivo.
- **Saque:** 
  - O número máximo de saques por dia é 3.
  - O valor máximo permitido por saque é de R$500,00.
  - O saldo da conta deve ser suficiente para realizar o saque.
- **Extrato:** Exibe o saldo atual da conta.
  

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
DIGITE A OPÇÃO DESEJADA:

[d] - Depositar 
[s] - Sacar 
[e] - Extrato Bancário 
[q] - Sair

=>
````


Você pode escolher a operação desejada digitando a letra correspondente.


## 📂 Estrutura do Código

- **exibir_saldo_conta(saldo):** Função que exibe o saldo atual da conta.
- **menu:** String que contém as opções do menu para interação com o usuário.
- **saldo_conta:** Variável que armazena o saldo atual da conta.
- **valor_limite_saque:** Limite máximo de valor por saque.
- **numero_saques:** Contador do número de saques realizados.
- **LIMITES_SAQUES:** Limite máximo de saques por dia.
- **Loop principal:** Onde as interações com o usuário acontecem, capturando a escolha e executando as operações correspondentes.

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
