# Boas-vindas ao repositório do projeto Consulta à uma API pública

## Do que se trata o repositório em questão?

Uma aplicação em python que consome dados de uma API chamada [JSONPlaceholder](https://jsonplaceholder.typicode.com/) que utiliza também as bibliotecas [Pytest](https://docs.pytest.org/en/stable/) , [Flask](https://flask.palletsprojects.com/en/stable/) e tem um frontend em [React.js](https://react.dev/).

A aplicação foi construída em python e consome a API JSONPlaceholder(```https://jsonplaceholder.typicode.com/```).


 <details>
  <summary><strong>📝 Os requisitos são:</strong></summary><br />

 - Consumir a API pública JSONPlaceholder para buscar dados de usuários e seus posts.
 - Exibir uma lista dos usuários com seus respectivos IDs e nomes.
 - Permitir que o usuário insira um ID de um usuário específico para:
 - Exibir o nome e o email do usuário selecionado.
 - Listar os títulos dos posts criados por esse usuário.
 - Tratar erros, como:
   - ID de usuário inválido
   - Problemas de conexão com a API
</details>

<details>
  <summary><strong>✅ Além dos requisitos, a aplicação entrega:</strong></summary><br />

 - Testes de Integração para a API utilizando pytest
 - API para ser consumida
 - Frontend em React
</details>

## Orientações

<details>
  <summary><strong>👨‍💻 Antes de começar:</strong></summary><br />

 - Crie o ambiente virtual executando o comando: ```python -m venv venv```
 - Aive o ambiente virtual execute os comandos:
   - No windows: ```venv\Scripts\activate```
   - No macOS ou Linux: ```source venv/bin/activate```
 - Instale as dependências executando o comando: ```pip install -r requirements.txt```
 - Para rodar a aplicação executando o comando: ```python src/main.py```
 - Para rodas os testes de integração de API executando o comando: ```set PYTHONPATH=src && pytest tests/test_api_service.py```

 Observação: Dessa forma a aplicação irá rodar no terminal conforme pedem os requisitos.
</details>

<details>
  <summary><strong>💅 Comandos personalizados:</strong></summary><br />

 - Criar, ativar o ambiente virtual e instalar as dependências: ```python manage.py instal```
 - Para rodar a aplicação: ```python manage.py start```

 Observação: Dessa forma a aplicação irá rodar no terminal conforme pedem os requisitos.
</details>

<details>
  <summary><strong>🚀 Comno rodar o FrontEnd e a API:</strong></summary><br />

 - Na raiz do projeto com o ambiente virtual ativado, execute o comando ```python app.py```
 - Em outro terminal acesse o diretório 'frontend' que encontrase na raíz do projeto e execute os comandos:
   - para instalar as dependências: ```npm install```
   - para rodar o frontend: ```npm start```
</details>


