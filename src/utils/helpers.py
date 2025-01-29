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

def get_user_input():
    """Solicita ao usuário um ID e retorna o número."""
    try:
        return int(input("\nDigite o ID do usuário para obter detalhes: "))
    except ValueError:
        print("ID inválido! Por favor, insira um número válido.")
        return None
