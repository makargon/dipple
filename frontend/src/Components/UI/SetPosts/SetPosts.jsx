import React, {useState, useEffect} from 'react';
import MyPost from '../MyPost/MyPost';
import axios from "axios";
import classes from "../SetPosts/SetPosts.module.css";

const SetPosts = () => {

  const [posts, setPosts] = useState([]);

  useEffect(() => {
    fetchPosts();
  } ,[]);

  async function fetchPosts() {
  let response = await axios.get("https://jsonplaceholder.typicode.com/posts");
  let data = response.data;
  setPosts(data);
  };

  return (
    <div>
      <div className={classes.posts}>
         {posts.map(post => 
      <MyPost key={post.id} post={post} to = {`/blog/${post.id}`}/>
      )}
      </div>
    </div>
  );  
};

export default SetPosts;