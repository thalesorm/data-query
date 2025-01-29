from services.api_service import get_users, get_user_details, get_posts_by_user

def display_users(users):
    """Exibe a lista de usuários com ID e nome."""
    if users:
        for user in users:
            print(f"ID: {user['id']} - Nome: {user['name']}")

def display_user_details(user):
    """Exibe os detalhes de um usuário (nome e e-mail)."""
    if user:
        print(f"Nome: {user['name']}")
        print(f"E-mail: {user['email']}")

def display_user_posts(posts):
    """Exibe os títulos dos posts de um usuário."""
    if posts:
        for post in posts:
            print(f"Título: {post['title']}")

def main():
    """Função principal que gerencia a interação com o usuário."""
    users = get_users()
    if not users:
        print("Não foi possível obter os usuários.")
        return

    display_users(users)

    try:
        user_id = int(input("\nDigite o ID do usuário para obter detalhes: "))
    except ValueError:
        print("ID inválido! Por favor, insira um número.")
        return

    # Obtém detalhes do usuário
    user = get_user_details(user_id)
    if user:
        display_user_details(user)

        # Obtém posts do usuário
        posts = get_posts_by_user(user_id)
        display_user_posts(posts)
    else:
        print("Usuário não encontrado!")

if __name__ == "__main__":
    main()
