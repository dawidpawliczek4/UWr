import React from "react";
import { FaCaretRight } from "react-icons/fa";
import WorkHistory from "./WorkHistory";

interface AboutProps {}

const About: React.FC<AboutProps> = ({}) => {
  return (
    <div>
      <div className="h-[calc(100vh-72px)] flex justify-center items-center pb-[72px]">
        <div className="w-1/2 flex flex-col gap-y-4">
          <h1 className="text-2xl">
            <span className="text-base text-violet-700">01.</span> About Me
          </h1>

          <p>
            I enjoy creating things that live on the internet, whether that be
            websites, applications, or anything in between. My goal is to always
            build products that provide pixel-perfect, performant experiences.
            My interest in web development started in high school, where I built
            my first website. I've been hooked ever since.
          </p>

          <p>
            Fast forward to today, and I've had the privilege of working at an
            advertising agency, a start-up, a huge corporation, and a student
            organization. My main focus these days is building accessible,
            inclusive products and digital experiences at Upstatement for a
            variety of clients.
          </p>

          <p>Here are few technologies I've been working with recently:</p>

          <ul className="grid grid-cols-2">
            <li className="flex items-center">
              <FaCaretRight className="text-violet-700" /> JavaScript
            </li>
            <li className="flex items-center">
              <FaCaretRight className="text-violet-700" /> TypeScript
            </li>
            <li className="flex items-center">
              <FaCaretRight className="text-violet-700" /> React
            </li>
            <li className="flex items-center">
              <FaCaretRight className="text-violet-700" /> Node.js
            </li>
            <li className="flex items-center">
              <FaCaretRight className="text-violet-700" /> Next.js
            </li>
            <li className="flex items-center">
              <FaCaretRight className="text-violet-700" /> Django
            </li>
          </ul>
        </div>
      </div>

      <div className="h-[400px] flex items-center justify-center">
        <div className="w-1/2 flex flex-col gap-y-4">
          <h1 className="text-2xl">
            <span className="text-base text-violet-700">02.</span> Where I've
            Worked
          </h1>
          <WorkHistory />
        </div>
      </div>
    </div>
  );
};

export default About;
