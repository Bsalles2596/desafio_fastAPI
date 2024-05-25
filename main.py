# Import 
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

# Define o modelo de dados para os clientes
class Cliente(BaseModel):
    id: int
    nome: str
    email: str
    telefone: str

# Inicializa a lista de clientes
clientes = []

@app.post("/clientes")
def criar_cliente(cliente: Cliente):
    """
    Adiciona um novo cliente à lista.
    """
    # Verifica se o ID já existe
    if any(c.id == cliente.id for c in clientes):
        raise HTTPException(status_code=400, detail="ID do cliente já existe")

    clientes.append(cliente)
    return cliente

@app.get("/clientes/{cliente_id}")
def obter_cliente(cliente_id: int):
    """
    Retorna os detalhes de um cliente específico pelo ID.
    """
    for cliente in clientes:
        if cliente.id == cliente_id:
            return cliente
    raise HTTPException(status_code=404, detail="Cliente não encontrado")
	
	
	
	## Aqui está uma explicação do código:
'''
Importamos as classes FastAPI e HTTPException do fastapi, e a classe BaseModel do pydantic.
Criamos uma instância da classe FastAPI chamada app.
Definimos o modelo de dados Cliente usando a classe BaseModel, que inclui os campos id, nome, email e telefone.
Inicializamos uma lista vazia chamada clientes para armazenar as informações dos clientes.
Criamos duas rotas:
POST /clientes: Adiciona um novo cliente à lista. Primeiro, verifica se o ID do cliente já existe. Se não, o cliente é adicionado à lista e retornado.
GET /clientes/{cliente_id}: Retorna os detalhes de um cliente específico pelo ID. Se o cliente não for encontrado, uma exceção HTTPException é lançada com o código de status 404 (Not Found).
Para executar a aplicação, use o seguinte comando:
'''
	# uvicorn main:app --reload

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

	# uvicorn main:app --reload
	
# Isso iniciará o servidor FastAPI e você poderá acessar a documentação interativa em http://localhost:8000/docs.



	

