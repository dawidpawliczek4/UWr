import React from "react";

interface HeaderProps {
  name: string;
  slogan: string;
}

const Header: React.FC<HeaderProps> = ({ name, slogan }) => {
  return (
    <header id="header" className="py-12 text-center">
      <div className="">
        <h1 className="text-5xl mb-3 font-bold">{name}</h1>
        <p className="text-2xl">{slogan}</p>
      </div>
    </header>
  );
};

export default Header;
