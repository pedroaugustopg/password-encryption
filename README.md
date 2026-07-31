# Sistema Bancário com Criptografia em Python

Projeto desenvolvido em Python com foco na aplicação de Programação Orientada a Objetos (POO), utilizando criptografia SHA-256 para armazenamento seguro de senhas e 
autenticação de operações sensíveis.

O sistema simula operações bancárias por meio de uma interface em terminal, permitindo a criação de contas, depósitos, saques e alteração do titular da conta.

Este projeto tem como finalidade praticar conceitos de desenvolvimento em Python, Programação Orientada a Objetos e fundamentos de segurança da informação, demonstrando
a utilização de criptografia para proteção de credenciais e autenticação de operações bancárias em ambiente de terminal.

## Funcionalidades

* Cadastro de contas bancárias
* Definição de senha durante a criação da conta
* Criptografia da senha utilizando SHA-256
* Autenticação obrigatória para operações protegidas
* Depósito em conta
* Saque com validação de saldo
* Alteração do titular mediante autenticação
* Exibição das informações da conta utilizando tabelas formatadas com a biblioteca Rich

## Tecnologias Utilizadas

* Python 3
* Rich
* hashlib (SHA-256)

## Conceitos Aplicados

* Programação Orientada a Objetos (POO)
* Encapsulamento
* Construtores
* Properties (`@property`)
* Setters (`@setter`)
* Hashing de senhas
* Criptografia com SHA-256
* Autenticação de usuários
* Validação de dados
* Type Hints
* Interface de terminal utilizando Rich

## Segurança

Um dos principais objetivos do projeto é demonstrar a aplicação de conceitos segurança da informação. As senhas **não são armazenadas em texto puro**. Durante o 
cadastro, a senha é convertida em um hash utilizando o algoritmo **SHA-256**, por meio da biblioteca padrão `hashlib`.

Sempre que uma operação protegida é executada, como um saque ou alteração do titular da conta, a senha informada é novamente criptografada e comparada com o hash 
armazenado, sem que a senha original seja exposta em nenhum momento.

Essa abordagem reduz significativamente o risco de vazamento de credenciais e segue uma prática amplamente utilizada em sistemas de autenticação.

## Regras de Negócio

* A senha deve possuir no mínimo 6 caracteres.
* As senhas são armazenadas apenas em formato criptografado (SHA-256).
* Operações protegidas exigem autenticação.
* Não é permitido realizar saques superiores ao saldo disponível.
* Valores depositados são adicionados ao saldo da conta.
* A alteração do titular somente é realizada após validação da senha.

## Estrutura do Projeto

```text
EncryptedPassword/
│
├── bankaccount/
│   ├── __main__.py
│   └── cripto.py
│
├── .gitignore
└── README.md
```

## Como Executar

Clone o repositório:

```bash
git clone(https://github.com/pedroaugustopg/password-encryption.git)
```

Acesse a pasta do projeto:

```bash
cd seu-repositorio
```

Execute a aplicação:

```bash
python -m bankaccount
```
