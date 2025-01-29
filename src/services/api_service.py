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
