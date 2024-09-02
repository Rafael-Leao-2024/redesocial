# Flask Blog Tutorial

Este é um tutorial de um blog simples e completo desenvolvido com Flask. Ele foi criado para ajudar iniciantes a aprender como construir uma aplicação web básica usando Flask.

## Visão Geral

Este projeto demonstra como criar um blog onde os usuários podem se registrar, fazer login, criar posts, editar posts, e deletar posts. Ele também inclui funcionalidades de autenticação para garantir que apenas usuários autenticados possam acessar certas páginas.

## Funcionalidades

- **Registro de Usuário:** Permite que novos usuários se registrem na aplicação.
- **Autenticação de Usuário:** Autenticação com gerenciamento de sessão para proteger páginas específicas.
- **Criação de Posts:** Usuários autenticados podem criar novos posts.
- **Edição e Deleção de Posts:** Posts podem ser editados ou deletados pelos seus autores.
- **Visualização de Posts:** Todos os usuários podem visualizar os posts publicados.

## Requisitos

Certifique-se de ter os seguintes pacotes instalados:

- Python 3.x
- Flask
- Flask-SQLAlchemy
- Flask-WTF
- Flask-Bcrypt
- Flask-Login

## Instalação

1. Clone este repositório:
    ```bash
    git clone https://github.com/Rafael-Leao-2024/redesocial.git
    ```
2. Navegue até o diretório do projeto:
    ```bash
    cd redesocial
    ```
3. Crie um ambiente virtual:
    ```bash
    python -m venv venv
    ```
4. Ative o ambiente virtual:
    - No Windows:
        ```bash
        venv\Scripts\activate
        ```
    - No macOS/Linux:
        ```bash
        source venv/bin/activate
        ```
5. Instale as dependências:
    ```bash
    pip install -r requirements.txt
    ```

## Como Usar

1. Crie o banco de dados e as tabelas:
    ```bash
    python
    >>> from app import db
    >>> with app.app_context():
    >>>     db.create_all()
    >>> exit()
    ```
2. Inicie o servidor:
    ```bash
    python run.py
    ```
3. Acesse a aplicação no navegador em `http://127.0.0.1:5000`.

## Estrutura do Projeto

- **pacote/**: Contém os arquivos da aplicação Flask.
  - **static/**: Arquivos estáticos (CSS, imagens, etc.).
  - **templates/**: Templates HTML.
  - **forms.py**: Formulários para registro, login, e posts.
  - **models.py**: Modelos do banco de dados.
  - **routes.py**: Rotas da aplicação.
  - **init.py**: Inicializa a aplicação Flask.
- **run.py**: Arquivo para iniciar o servidor.
- **requirements.txt**: Lista de dependências do projeto..

## Contribuição

Sinta-se à vontade para fazer um fork deste projeto e contribuir com melhorias! Abra um pull request com suas mudanças.

## Licença

Este projeto está licenciado sob a licença MIT. Veja o arquivo `LICENSE` para mais detalhes.
