import React from "react";

interface SectionContentProps {
  children: React.ReactNode;
}

const SectionContent: React.FC<SectionContentProps> = ({ children }) => {
  return <div className="max-w-3xl mx-auto my-0">{children}</div>;
};

export default SectionContent;
