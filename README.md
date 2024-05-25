# Desafio FastAPI
## Aplicação CRUD Básica:

## Aqui está uma explicação do código:
--- 

Importado as classes FastAPI e HTTPException do fastapi, e a classe BaseModel do pydantic.
Criado uma instância da classe FastAPI chamada app.
Definido o modelo de dados Cliente usando a classe BaseModel, que inclui os campos id, nome, email e telefone.
Inicializado uma lista vazia chamada clientes para armazenar as informações dos clientes.
Criado duas rotas:
POST /clientes: Adiciona um novo cliente à lista. Primeiro, verifica se o ID do cliente já existe. Se não, o cliente é adicionado à lista e retornado.
GET /clientes/{cliente_id}: Retorna os detalhes de um cliente específico pelo ID. Se o cliente não for encontrado, uma exceção HTTPException é lançada com o código de status 404 (Not Found).
--

## Instruções de configuração e execução:

### Certifique-se de ter o Python 3.7 ou superior instalado.
### Crie um ambiente virtual venv.

## Comando para criar o ambiente Virtual no Windows, terminal usado powershell.

~~~
   $   python -m venv venv  
~~~

### Comando para Ativar ambiente virtual venv no terminal powershell;
 
~~~
   $   #cd .\venv\Scripts\Activate.Ps1     
~~~

### Após ativar o ambiente Virtual.
### Instale todos pacotes nescessarios para execução :

~~~
   $   pip install -r requirements.txt
~~~

## Executando:

~~~
   $  uvicorn main:app --reload
~~~

## Isso iniciará o servidor FastAPI e você poderá acessar a documentação interativa em http://localhost:8000/docs.

### Você pode testar as rotas usando ferramentas como o Postman ou o cURL. 
## Por exemplo, para adicionar um novo cliente:

   # curl http://localhost:8000/clientes

body

   {
   "id": 5,
   "nome": "Joao",
   "email": "joao@gmail.com",
   "telefone": "62995216889"
   }

### E para obter os detalhes de um cliente:

	# curl http://localhost:8000/clientes/5
	
## Este código implementa as seguintes funcionalidades:

### Definição do modelo de dados Cliente usando Pydantic.
### Simulação de um banco de dados em memória usando uma lista chamada clientes.
### Implementação da rota POST /clientes/ para criar um novo cliente.

## Exemplo de uso:

### Implementação da rota GET /clientes/{cliente_id} para obter os detalhes de um cliente específico.	

# Testes unitários com cobertura

## Para executar os testes, você pode usar o seguinte comando:

~~~
   $  pytest
~~~
	
### Isso irá executar os testes e exibir os resultados.
---

Para visualizar o projeto completo acesse repositório do Github ou do Gitlab e fique à vontade para brincar o quanto quiser:

[Repositório Github](https://github.com/)





