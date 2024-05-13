import React from "react";

interface AboutProps {
    about: string;
}

const About: React.FC<AboutProps> = ({about}) => {
  return (
    <div>
      <h2 className="font-semibold">About Us</h2>
      <p>{about}</p>
    </div>
  );
};

export default About;
