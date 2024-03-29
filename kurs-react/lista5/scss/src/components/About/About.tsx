import React from "react";

const About = ({ about }: { about: string }) => {
  return (
    <>
      <h2>About Us</h2>
      <p>{about}</p>
    </>
  );
};

export default About;
