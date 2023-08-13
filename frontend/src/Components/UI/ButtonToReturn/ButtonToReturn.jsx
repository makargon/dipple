import React from 'react';
import './ButtonToReturn.css';

const ButtonToReturn = () => {

  const [scroll, setScroll] = React.useState(0);

  const handleScroll = () => {
    setScroll(window.scrollY);
  };

  const handleUpButton = () => {
    window.scrollTo({
      top: 0,
      left: 0,
      behavior: 'smooth'
    });
  };

  React.useEffect(() => {
    window.addEventListener("scroll", handleScroll);
    return () => window.removeEventListener("scroll", handleScroll);
  }, []);

  return (
    <div>
     <button className={scroll < 600 ? "btnHide" : "btnShow"} onClick = {handleUpButton}>🠕</button>    
    </div>
  );
};

export default ButtonToReturn;