import React from "react";

interface SaveButtonProps {
  children: React.ReactNode;
}

const SaveButton: React.FC<SaveButtonProps> = ({ children }) => {
  return (
    <button className="inline-flex items-center justify-center rounded px-[15px] text-[15px] leading-none font-medium h-[35px] bg-green10 text-green4 hover:bg-green11 focus:shadow-[0_0_0_2px] focus:shadow-green10 outline-none cursor-pointer">
      {children}
    </button>
  );
};

export default SaveButton;
