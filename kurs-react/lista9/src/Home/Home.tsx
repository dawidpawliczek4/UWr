import React from "react";
import { FaGithub, FaLinkedin } from "react-icons/fa";

interface HomeProps {}

const Home: React.FC<HomeProps> = ({}) => {
  return (
    <div className="h-[calc(100vh-72px)] flex justify-center items-center w-3/5 mx-auto">
      <div className="flex flex-col w-1/2 gap-y-2">
        <h1 className="text-6xl">
          Hey, I'm <span className="text-violet-700">Dawid</span> 👋
        </h1>
        <p className="">
          I'm a junior fullstack developer and Computer Science student at the
          University of Wrocław. As a developer I take on several different
          projects creating mostly web applications.
        </p>
        <div className="flex gap-x-4 justify-center text-white/80">
          <a href="https://github.com/dawidpawliczek4">
            <FaGithub className="text-2xl" />
          </a>
          <a href="https://www.linkedin.com/in/dawid-pawliczek-43376a285/">
            <FaLinkedin className="text-2xl" />
          </a>
        </div>
      </div>
      <div className="w-1/2 flex justify-center items-center">
        There will be image here
      </div>
    </div>
  );
};

export default Home;
