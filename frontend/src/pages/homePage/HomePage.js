import React, { useState, useEffect } from "react";
import { Link } from "react-router-dom";
import { getUsers } from "../../api/apiService";
import "./HomePage.css";

const HomePage = () => {
  const [users, setUsers] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchUsers = async () => {
      try {
        const data = await getUsers();
        if (data) {
          setUsers(data);
        }
      } catch (err) {
        setError("Não foi possível carregar os dados.");
      } finally {
        setLoading(false);
      }
    };
    fetchUsers();
  }, []);

  if (loading) return <p>Carregando...</p>;
  if (error) return <p>{error}</p>;

  return (
    <div>
      <h1>Consumindo a API do Projeto</h1>
      <table className="user-list-table">
        <thead>
          <tr>
            <th>ID</th>
            <th>Nome</th>
          </tr>
        </thead>
        <tbody>
          {users.length > 0 ? (
            users.map((user) => (
              <tr key={user.id}>
                <td>{user.id}</td>
                <td>
                  <Link to={`/users/${user.id}`}>{user.name}</Link>
                </td>
              </tr>
            ))
          ) : (
            <tr>
              <td colSpan="2" style={{ textAlign: "center" }}>
                Nenhum usuário encontrado. Verificou se a API está rodando?
              </td>
            </tr>
          )}
        </tbody>
      </table>
    </div>
  );
};

export default HomePage;
