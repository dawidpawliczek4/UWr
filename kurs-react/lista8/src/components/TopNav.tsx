import React from "react";

interface TopNavProps {
  darkMode: boolean;
  toggleTheme: () => void;
}

const TopNav: React.FC<TopNavProps> = ({ darkMode, toggleTheme }) => {
  return (
    <div className="sticky top-0 py-4 text-center z-10 bg-[#f0f0f0] dark:bg-[#222]">
      <a href="#header" className="px-5 ">
        Home
      </a>
      <a href="#about" className="px-5">
        About
      </a>
      <a href="#services" className="px-5">
        Services
      </a>
      <a href="#team" className="px-5">
        Team
      </a>
      <a href="#blog" className="px-5">
        Blog
      </a>
      <a href="#contact" className="px-5">
        Contact
      </a>
      <button
        onClick={toggleTheme}
        className="cursor-pointer px-4 py-2 bg-[#333] text-white rounded-md hover:bg-[#555]
    dark:bg-[#ddd] dark:text-[#333] dark:hover:bg-[#ccc] transition-colors duration-300 ease-in-out
    "
      >
        {darkMode ? "Light Mode" : "Dark Mode"}
      </button>
    </div>
  );
};

export default TopNav;
