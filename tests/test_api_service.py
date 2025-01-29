import unittest
from unittest.mock import patch
from services.api_service import get_users, get_user_details, get_posts_by_user

class TestApiService(unittest.TestCase):

    @patch('services.api_service.requests.get')
    def test_get_users_success(self, mock_get):
        """Testa se get_users retorna uma lista de usuários corretamente."""
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = [
            {"id": 1, "name": "Usuário Teste"},
            {"id": 2, "name": "Outro Usuário"}
        ]

        users = get_users()
        self.assertIsInstance(users, list)
        self.assertEqual(len(users), 2)
        self.assertEqual(users[0]['name'], "Usuário Teste")

    @patch('services.api_service.requests.get')
    def test_get_user_details_success(self, mock_get):
        """Testa se get_user_details retorna os detalhes corretos de um usuário."""
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = {"id": 1, "name": "Usuário Teste", "email": "teste@email.com"}

        user = get_user_details(1)
        self.assertIsNotNone(user)
        self.assertEqual(user['name'], "Usuário Teste")
        self.assertEqual(user['email'], "teste@email.com")

    @patch('services.api_service.requests.get')
    def test_get_posts_by_user_success(self, mock_get):
        """Testa se get_posts_by_user retorna os posts corretamente."""
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = [
            {"userId": 1, "id": 101, "title": "Primeiro Post"},
            {"userId": 1, "id": 102, "title": "Segundo Post"}
        ]

        posts = get_posts_by_user(1)
        self.assertIsInstance(posts, list)
        self.assertEqual(len(posts), 2)
        self.assertEqual(posts[0]['title'], "Primeiro Post")

if __name__ == '__main__':
    unittest.main()
