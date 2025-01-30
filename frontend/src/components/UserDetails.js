import React, { useEffect, useState } from "react";
import { getUserDetails } from "../api/apiService";
import { useParams } from "react-router-dom";
import UserPosts from "./UserPosts";

const UserDetails = () => {
  const { userId } = useParams();
  const [user, setUser] = useState(null);
  const [loading, setLoading] = useState(true);
  const [showPosts, setShowPosts] = useState(false);

  useEffect(() => {
    const fetchUserData = async () => {
      const userData = await getUserDetails(userId);
      if (userData) {
        setUser(userData);
      }
      setLoading(false);
    };
    fetchUserData();
  }, [userId]);

  if (loading) return <p>Carregando...</p>;

  if (!user) return <p>Usuário não encontrado.</p>;

  return (
    <div>

    <div>
      <h2>{user.name}</h2>
      <p>E-mail: {user.email}</p>
      <button onClick={() => setShowPosts(!showPosts)}>
        {showPosts ? "Ocultar Posts" : "Carregar Posts"}
      </button>

      {showPosts && <UserPosts userId={userId} />}
    </div>
    </div>
  );
};

export default UserDetails;
