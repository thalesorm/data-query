from flask import Flask, jsonify, request
from flask_cors import CORS
from src.services.api_service import get_users, get_user_details, get_posts_by_user
from src.utils.helpers import display_users, display_user_details, display_user_posts

app = Flask(__name__)

CORS(app)

@app.route('/')
def home():
    """Página inicial."""
    return "Bem-vindo à API de usuários!"

@app.route('/users', methods=['GET'])
def users():
    """Obtém todos os usuários."""
    users_data = get_users()
    if users_data:
        return jsonify(users_data), 200
    return jsonify({"message": "Não foi possível obter os usuários."}), 500

@app.route('/users/<int:user_id>', methods=['GET'])
def user_details(user_id):
    """Obtém os detalhes de um usuário específico."""
    user_data = get_user_details(user_id)
    if user_data:
        return jsonify(user_data), 200
    return jsonify({"message": "Usuário não encontrado."}), 404

@app.route('/users/<int:user_id>/posts', methods=['GET'])
def user_posts(user_id):
    """Obtém os posts de um usuário específico."""
    posts_data = get_posts_by_user(user_id)
    if posts_data:
        return jsonify(posts_data), 200
    return jsonify({"message": "Posts não encontrados."}), 404

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
