import React from 'react';
import classes from "../Footer/Footer.module.css";

const Footer = () => {
  return (
    <ul className={classes.footerNavbar}>
      <img src= '../images/footerLogo1.png' alt="Изображение не загружено..." className={classes.navTitle}/>
      <img src= '../images/footerLogo2.png' alt="Изображение не загружено..." className={classes.navTitle}/>
      <img src= '../images/footerLogo3.png' alt="Изображение не загружено..." className={classes.navTitle}/>
    </ul>
  );
};

export default Footer;