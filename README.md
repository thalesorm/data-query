# Boas-vindas ao repositório do projeto Consulta à uma API pública

## Do que se trata o repositório em questão?

Uma aplicação em python que consome dados de uma API chamada [JSONPlaceholder](https://jsonplaceholder.typicode.com/) que utiliza também as bibliotecas [Pytest](https://docs.pytest.org/en/stable/) , [Flask](https://flask.palletsprojects.com/en/stable/) e tem um frontend em [React.js](https://react.dev/).

A aplicação foi construída em python e consome a API [JSONPlaceholder](https://jsonplaceholder.typicode.com/).

O Deploy da aplicação foi feito no vercel e pode ser acessado no seguinte link: 
https://data-querty-app.vercel.app/

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
 - [Deploy]() da aplicação usando [Vercel](https://vercel.com/)
</details>

## Orientações

<details>
  <summary><strong>👨‍💻 Antes de começar:</strong></summary><br />

 - No seu terminal, clone o repositório executando o comando: ```git clone https://github.com/thalesorm/data-query.git```
 - Certifique-se de ter o [Python](C:\Users\Thales\Documents\python\data-query\app.py) instalado na sua máquina
 - Execute no terminal: ```cd data-query```
 - Caso queria abrir o [Visual Studio Code](https://code.visualstudio.com/), execute o comando ```code .```
 - Caso esteja seu SO seja Windows certifique-se de está usando o cmd *(Command Pronpt)*
 - Crie o ambiente virtual executando o comando: ```python -m venv venv```
 - Ative o ambiente virtual executando os comandos:
   - No windows: ```venv\Scripts\activate```
   - No macOS ou Linux: ```source venv/bin/activate```
 - Instale as dependências executando o comando: ```pip install -r requirements.txt```
 - Para rodar a aplicação execute o comando: ```python src/main.py```
 - Para rodar os testes de integração de API execute o comando: ```set PYTHONPATH=src && pytest tests/test_api_service.py```

 Observação: Dessa forma a aplicação irá rodar no terminal conforme pedem os requisitos.
</details>

<details>
  <summary><strong>💅 Comandos personalizados:</strong></summary><br />

 - Criar o ambiente virtual e instalar as dependências: ```python manage.py install```
 - Para rodar a aplicação: ```python manage.py start```

 Observação: Dessa forma a aplicação irá rodar no terminal conforme pedem os requisitos.
</details>

<details>
  <summary><strong>🚀 Como rodar o FrontEnd e a API:</strong></summary><br />

 - Na raiz do projeto com o ambiente virtual ativado, execute o comando ```python app.py```
 - Em outro terminal acesse o diretório 'frontend' usando o comando ```cd frontend``` que encontra-se na raíz do projeto e execute os comandos:
   - para instalar as dependências: ```npm install```
   - para rodar o frontend: ```npm start```
   - A aplicação irá rodar na url ```http://localhost:3000```
</details>

<details>
  <summary><strong>🐳 Como rodar a aplicação com Docker:</strong></summary><br />

 - Certifique-se de ter o [Docker](https://www.docker.com/) instalado e executando em sua máquina
 - Crie uma códia do arquivo ```.env.example``` e renomei para ```.env```
 - cole o comando dentro do novo arquivo ```.env``` o seguinte comando: ```REACT_APP_BACKEND_URL=http://localhost:5000```
 - Na raiz do projeto execute o comando ```docker-compose up --build```
 - O front pode ser acessado na url ```http://127.0.0.1:3000/```
 - A API pode ser acessada na url ```http://127.0.0.1:5000/```
</details>
