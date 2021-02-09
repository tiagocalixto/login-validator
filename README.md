# Login Validator

### Objetivo
Projeto desenvolvido com intuito de validar se uma senha é valida ou não de acordo com os seguintes critérios:

- Nove ou mais caracteres
- Ao menos 1 dígito
- Ao menos 1 letra minúscula
- Ao menos 1 letra maiúscula
- Ao menos 1 caractere especial(Considere como especial os seguintes caracteres: !@#$%^&*()-+)
- Não possuir caracteres repetidos dentro do conjunto

### Stack
- Aplicação desenvolvida em Python 3.8.5
- Framework Flask 
- Sistema operacional Linux Ubunto
- Ide Pycharm community
- Testes com UnitTest e Pytest

### Motivação
Atualmente sou desenvolvedor Java e praticamente meu dia a dia de trabalho é desenvolvendo na linguagem. Para sair da rotina e também tornar o desafio mais interessante, decidi utilizar Python com framework Flask para o desenvolvimento dessa app, além de python ser uma linguagem de programação que eu particularmente gosto bastante, aproveitei para aprender Flask, tecnologia do qual não tinha conhecimento algum anteriormente. Para arquitetura do projeto eu me inspirei na Clean Architecture, utilizando SOLID e boas práticas ensinadas no Clean Code. 

### Pré Requisitos
- Python 3.8 ou superior -> instalação varia de acordo com o sistema operacional
- PIP -> gerenciador de pacotes python, sua instalção varia de acordo com sistema operacional
- Virtualenv -> ambiente virtual para cada projeto, evitando que as dependencias sejam instaladas diretamente no sistema operacional
  - Para instalar o virtualEnv basta utilizar o comando 'pip install virtualenv'
- Recomendável utilização da IDE Pycharm community ou visual studio code
  
### Preparar o Ambiente Para Execução do Projeto Local
Após abrir o projeto, executar os comandos abaixo no terminal da própria IDE:

- Ativar o ambiente virtual
  - 'python3 -m venv venv'
  - 'source venv/bin/activate'
  
- Instalar todas dependencias
  - 'pip install -r requirements.txt'
  
- Setar variáveis de ambiente do Flask
  - 'export FLASK_APP=src/controller/controller.py'
  - 'export FLASK_DEBUG=1'
  
### Executar o Projeto Local
- 'python -m flask run'

### Executar Testes Unitários Local
- 'pytest -rp'
