import requests

API_URL = "https://jsonplaceholder.typicode.com"

def get_users():
    """Obtém a lista de usuários da API."""
    try:
        response = requests.get(f"{API_URL}/users")
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Erro ao fazer a requisição: {e}")
        return None
    
def get_user_details(user_id):
    """Obtém os detalhes de um usuário específico (nome e e-mail)."""
    try:
        response = requests.get(f"{API_URL}/users/{user_id}")
        response.raise_for_status()  # Levanta exceção para erros HTTP
        return response.json()  # Retorna a resposta no formato JSON
    except requests.exceptions.RequestException as e:
        print(f"Erro ao fazer a requisição: {e}")
        return None
    
