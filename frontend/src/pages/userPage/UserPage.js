import React, { useEffect, useState } from "react";
import { useParams, useNavigate } from "react-router-dom";
import { getUserDetails } from "../../api/apiService";
import UserPosts from "../../components/UserPosts";
import "./UserPage.css";

const UserPage = () => {
  const { userId } = useParams();
  const [user, setUser] = useState(null);
  const [loading, setLoading] = useState(true);
  const [showPosts, setShowPosts] = useState(false);
  const navigate = useNavigate();

  useEffect(() => {
    const fetchUser = async () => {
      const data = await getUserDetails(userId);
      if (data) {
        setUser(data);
      }
      setLoading(false);
    };
    fetchUser();
  }, [userId]);

  if (loading) return <p>Carregando...</p>;

  return (
    <div className="user-page-container">
      <button className="back-button" onClick={() => navigate(-1)}>
        &#8592; Voltar
      </button>
      <h2>Detalhes do Usuário</h2>
      {user ? (
        <div className="user-details">
          <p><strong>Nome:</strong> {user.name}</p>
          <p><strong>Email:</strong> {user.email}</p>
          <button
            onClick={() => setShowPosts(!showPosts)}
          >
            {showPosts ? "Ocultar Posts" : "Carregar Posts"}
          </button>

          {showPosts && (
            <div className="posts-table-container">
              <table className="posts-table">
                <thead>
                  <tr>
                    <th>Título</th>
                    <th>Conteúdo</th>
                  </tr>
                </thead>
                <tbody>
                  <UserPosts userId={userId} />
                </tbody>
              </table>
            </div>
          )}
        </div>
      ) : (
        <p>Usuário não encontrado.</p>
      )}
    </div>
  );
};

export default UserPage;
