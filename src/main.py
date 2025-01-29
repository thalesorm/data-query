from services.api_service import get_users

def display_users(users):
    """Exibe a lista de usuários com ID e nome."""
    if users:
        for user in users:
            print(f"ID: {user['id']} - Nome: {user['name']}")

def main():
    """Função principal pra gerenciar a interação com o usuário."""
    users = get_users()
    if not users:
        print("Não foi possível obter os usuários.")
        return

    display_users(users)

if __name__ == "__main__":
    main()
