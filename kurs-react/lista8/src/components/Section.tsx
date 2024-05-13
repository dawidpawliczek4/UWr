import React from "react";
import SectionContent from "./SectionContent";

interface SectionProps {
  children: React.ReactNode;
  id: string;
}

const Section: React.FC<SectionProps> = ({ children, id }) => {
  return (
    <section id={id} className={"py-5 even:bg-[#f5f5f5] dark:even:bg-[#444]"}>
      <SectionContent>{children}</SectionContent>
    </section>
  );
};

export default Section;
