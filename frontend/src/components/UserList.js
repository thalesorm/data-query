import React, { useEffect, useState } from "react";
import { getUsers } from "../api/apiService";
import { Link } from "react-router-dom";

const UserList = () => {
  const [users, setUsers] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const fetchUsers = async () => {
      const data = await getUsers();
      if (data) {
        setUsers(data);
      }
      setLoading(false);
    };
    fetchUsers();
  }, []);

  if (loading) return <p>Carregando...</p>;

  return (
    <div>
      <h2 style={{ fontSize: "24px", marginBottom: "10px" }}>Lista de Usuários</h2>
      <table style={{ width: "100%", borderCollapse: "collapse", margin: "20px 0" }}>
        <thead>
          <tr>
            <th style={{ padding: "12px", textAlign: "left", border: "1px solid #ddd", backgroundColor: "#f2f2f2" }}>ID</th>
            <th style={{ padding: "12px", textAlign: "left", border: "1px solid #ddd", backgroundColor: "#f2f2f2" }}>Nome</th>
          </tr>
        </thead>
        <tbody>
          {users.map((user) => (
            <tr key={user.id} style={{ backgroundColor: "#f9f9f9" }}>
              <td style={{ padding: "12px", textAlign: "left", border: "1px solid #ddd" }}>{user.id}</td>
              <td style={{ padding: "12px", textAlign: "left", border: "1px solid #ddd" }}>
                <Link to={`/users/${user.id}`} style={{ color: "#333", textDecoration: "none" }}>
                  {user.name}
                </Link>
              </td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
};


export default UserList;
