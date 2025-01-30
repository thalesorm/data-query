const API_URL = "http://localhost:5000";

export const getUsers = async () => {
  try {
    const response = await fetch(`${API_URL}/users`);
    console.log("Response status:", response.status);
    if (!response.ok) {
      throw new Error("Erro ao obter usuários.");
    }
    const data = await response.json();
    console.log('Users data:', data);
    return data;
  } catch (error) {
    console.error("Error fetching users:", error);
    return null;
  }
};


export const getUserDetails = async (userId) => {
  try {
    const response = await fetch(`${API_URL}/users/${userId}`);
    if (!response.ok) {
      throw new Error("Erro ao obter detalhes do usuário.");
    }
    return await response.json();
  } catch (error) {
    console.error(error);
    return null;
  }
};


export const getUserPosts = async (userId) => {
  try {
    const response = await fetch(`${API_URL}/users/${userId}/posts`);
    if (!response.ok) {
      throw new Error("Erro ao obter posts do usuário.");
    }
    return await response.json();
  } catch (error) {
    console.error(error);
    return null;
  }
};