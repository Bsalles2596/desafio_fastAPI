# Desafio FastAPI
## Aplicação CRUD Básica:

## Aqui está uma explicação do código:

Importamos as classes FastAPI e HTTPException do fastapi, e a classe BaseModel do pydantic.
Criamos uma instância da classe FastAPI chamada app.
Definimos o modelo de dados Cliente usando a classe BaseModel, que inclui os campos id, nome, email e telefone.
Inicializamos uma lista vazia chamada clientes para armazenar as informações dos clientes.
Criamos duas rotas:
POST /clientes: Adiciona um novo cliente à lista. Primeiro, verifica se o ID do cliente já existe. Se não, o cliente é adicionado à lista e retornado.
GET /clientes/{cliente_id}: Retorna os detalhes de um cliente específico pelo ID. Se o cliente não for encontrado, uma exceção HTTPException é lançada com o código de status 404 (Not Found).
Para executar a aplicação, use o seguinte comando:

--

## Instruções de configuração e execução:

# Certifique-se de ter o Python 3.7 ou superior instalado.
# Crie um ambiente virtual e ative-o.

### Instale as dependências:

~~~
   $   pip install fastapi uvicorn pytest
~~~

# Salve o código da aplicação em um arquivo chamado main.py.
# Salve o código de teste em um arquivo chamado test_main.py.

===

~~~
   $  uvicorn main:app --reload
~~~

# Você pode testar as rotas usando ferramentas como o Postman ou o cURL. 
# Por exemplo, para adicionar um novo cliente:

# E para obter os detalhes de um cliente:

	# curl http://localhost:8000/clientes/1
	
## Este código implementa as seguintes funcionalidades:

# Definição do modelo de dados Cliente usando Pydantic.
# Simulação de um banco de dados em memória usando uma lista chamada clientes.
# Implementação da rota POST /clientes/ para criar um novo cliente.

# Exemplo de uso:

# Implementação da rota GET /clientes/{cliente_id} para obter os detalhes de um cliente específico.	

### Para executar a aplicação, salve este código em um arquivo chamado main.py e execute o seguinte comando:
---

~~~
   $  uvicorn main:app --reload
~~~


# Isso iniciará o servidor FastAPI e você poderá acessar a documentação interativa em http://localhost:8000/docs.



### Para executar os testes, você pode usar o seguinte comando:

~~~
   $  pytest
~~~

	
#Isso irá executar os testes e exibir os resultados.
---


Para visualizar o projeto completo acesse repositório do Github ou do Gitlab e fique à vontade para brincar o quanto quiser:

[Repositório Github](https://github.com/python-curso/rest-api/)
 | [Repositório Gitlab](https://gitlab.com/python-curso/rest-api)





