import React from "react";

interface FooterProps {
  name: string;
}

const Footer: React.FC<FooterProps> = ({ name }) => {
  return (
    <footer className="py-5 text-center">
      <div className="">
        <p>
          &copy; {new Date().getFullYear()} {name}
        </p>
      </div>
    </footer>
  );
};

export default Footer;
