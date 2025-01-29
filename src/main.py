from services.api_service import get_users, get_user_details, get_posts_by_user
from utils.helpers import display_users, display_user_details, display_user_posts, get_user_input

def main():
    """Função principal que gerencia a interação com o usuário."""
    users = get_users()
    if not users:
        print("Não foi possível obter os usuários.")
        return

    display_users(users)

    user_id = get_user_input()
    if user_id is None:
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
