## Testes unitários para verificar a funcionalidade da aplicação:
#import
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

## Estes testes verificam as seguintes situações:

# Criação de um novo cliente.

def test_criar_cliente():
    response = client.post("/clientes/", json={"id": 1, "nome": "João Silva", "email": "joao@example.com", "telefone": "123456789"})
    assert response.status_code == 200
    assert response.json()["id"] == 1
    assert response.json()["nome"] == "João Silva"
    assert response.json()["email"] == "joao@example.com"
    assert response.json()["telefone"] == "123456789"

# Obtenção dos detalhes de um cliente existente.

def test_obter_cliente():
    client.post("/clientes/", json={"id": 3, "nome": "Maria Souza", "email": "maria@example.com", "telefone": "987654321"})
    response = client.get("/clientes/3")
    print(client)
    assert response.status_code == 200
    assert response.json()["id"] == 3
    assert response.json()["nome"] == "Maria Souza"
    assert response.json()["email"] == "maria@example.com"
    assert response.json()["telefone"] == "987654321"

# Obtenção de um cliente que não existe (retorna 404).

def test_cliente_nao_encontrado():
    response = client.get("/clientes/999")
    assert response.status_code == 404
    assert response.json()["detail"] == "Cliente não encontrado"



### Para executar os testes, você pode usar o seguinte comando:

	# pytest
	
#Isso irá executar os testes e exibir os resultados.

## Instruções de configuração e execução:

#Certifique-se de ter o Python 3.7 ou superior instalado.
#Crie um ambiente virtual e ative-o.

### Instale as dependências:

	# pip install fastapi uvicorn pytest
	
# Salve o código da aplicação em um arquivo chamado main.py.
# Salve o código de teste em um arquivo chamado test_main.py.

### Execute a aplicação

	# uvicorn main:app --reload
	
### Execute os testes:

	# pytest
