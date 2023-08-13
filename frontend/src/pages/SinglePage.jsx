import React, {useState, useEffect} from 'react';
import { useParams } from 'react-router-dom';
import axios from 'axios';

export const SinglePage = () => {

  const {id} = useParams();

  const [post, setPost] = useState('');

  useEffect(() => {
    fetchPosts();
  } ,[id]);

  async function fetchPosts() {
  let response = await axios.get(`https://jsonplaceholder.typicode.com/posts/${id}`);
  let data = response.data;
  setPost(data);
  };

  return (
    <div>
      <h1 style={{marginTop: "30px"}}>{post.id}. {post.title}</h1>
      <p>{post.body}</p>
    </div>
  );
};

export default SinglePage;