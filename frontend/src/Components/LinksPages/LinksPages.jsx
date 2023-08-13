import React from 'react';
import { Outlet, NavLink } from 'react-router-dom';
import Navbar from '../UI/Navbar/Navbar';
import '../LinksPages/LinksPages.css';

export const LinksPages = () => {
  return (
    <>
    <Navbar/>
    <header>
      <NavLink to="/blog"      className="navLink">Blog</NavLink>
      <NavLink to="/homePages" className="navLink">HomePages</NavLink>
    </header>
    <Outlet />
    </>
  );
};

export default LinksPages;