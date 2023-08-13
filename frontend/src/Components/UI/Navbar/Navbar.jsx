import React, { useState, useMemo } from 'react';
import classes from "../Navbar/Navbar.module.css";

const Navbar = () => {

  let days = ["Воскресенье", "Понедельник", "Вторник", "Среда", "Четверг","Пятница","Суббота"];

 const [dayOfTheWeek, setDayOfTheWeek] = useState(0);
 
 useMemo(() => {
    setDayOfTheWeek(() => new Date().getDay())
 }, []);

  return (
    <header>
    <img className={classes.logoDipple} src= '../images/avatar.jpg' alt="Изображение не загружено..." />
    <div className={classes.dayOfTheWeek}>{days[dayOfTheWeek]}</div>
   </header>
  );
};

export default Navbar;