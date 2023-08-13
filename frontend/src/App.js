import React from "react";
import classes from "../src/styles/App.module.css";
import { Routes, Route } from "react-router-dom";

// pages
import {Blog} from './pages/Blog';
import {SinglePage} from './pages/SinglePage';
import {HomePages} from './pages/HomePages';
import {LinksPages} from "./Components/LinksPages/LinksPages";

function App() {

  return (
    <div className={classes.App}>
        <Routes>
          <Route path="/" element={<LinksPages />}>
            <Route path="homePages" element={<HomePages />}/>
            <Route path="blog" element={<Blog />}/>
            <Route path="blog/:id" element={<SinglePage />}/>
            <Route path="*" element={<Blog />}/>
          </Route>
        </Routes>
        
    </div>
   
  );
}

export default App;
