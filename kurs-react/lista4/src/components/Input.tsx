import React from "react";

const Input = ({
  onChange,
  placeholder,
  className,
  type = "text",
  value,
}: {
  onChange: (e: React.ChangeEvent<HTMLInputElement>) => void;
  placeholder: string;
  className?: string;
  type?: string;
  value: string;
}) => {
  return (
    <input
      type={type}
      placeholder={placeholder}
      className={`border-black-300 border-2 rounded-md p-2 ${className}`}
      value={value}
      onChange={onChange}
    />
  );
};

export default Input;
