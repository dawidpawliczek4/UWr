import React from "react";

interface SectionProps {
  children: React.ReactNode;
  id: string;
  className: string;
}

const Section: React.FC<SectionProps> = ({ children, id, className }) => {
  return (
    <section id={id} className={"blabla" + " " + className}>
      {children}
    </section>
  );
};

export default Section;
