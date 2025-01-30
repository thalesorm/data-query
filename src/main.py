from services.api_service import get_users, get_user_details, get_posts_by_user
from utils.helpers import display_users, display_user_details, display_user_posts, get_user_input

def main():
    while True:
        """Função principal que gerencia a interação com o usuário."""
        users = get_users()
        if not users:
            print("Não foi possível obter os usuários.")
            return

        display_users(users)

        user_id = get_user_input()
        print(f"ID do usuário: {user_id}") 

        if user_id is None:
            print("ID de usuário inválido!")
            continue

        user = get_user_details(user_id)
        if user:
            display_user_details(user)

            posts = get_posts_by_user(user_id)
            display_user_posts(posts)
        else:
            print("Usuário não encontrado!")

        action = input("\nDigite 1 para voltar e 0 para parar: ")

        if action == "0":
            print("Aplicação encerrada.")
            break
        elif action != "1":
            print("Opção inválida! Por favor, digite 1 para voltar ou 0 para parar.")
            continue

if __name__ == "__main__":
    main()
