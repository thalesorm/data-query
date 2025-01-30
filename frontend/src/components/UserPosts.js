import React, { useEffect, useState } from "react";
import { getUserPosts } from "../api/apiService";

const UserPosts = ({ userId }) => {
  const [posts, setPosts] = useState([]);

  useEffect(() => {
    const fetchPosts = async () => {
      const postsData = await getUserPosts(userId);
      if (postsData) {
        setPosts(postsData);
      }
    };
    fetchPosts();
  }, [userId]);

  return (
    <>
      {posts.map((post) => (
        <tr key={post.id}>
          <td>{post.title}</td>
          <td>{post.body}</td>
        </tr>
      ))}
    </>
  );
};

export default UserPosts;
