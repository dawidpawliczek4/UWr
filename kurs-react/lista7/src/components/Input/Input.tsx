import React from "react";

interface InputProps {
  id: string;
  defaultValue?: string;
  label: string;
  type?: string;
}

const Input: React.FC<InputProps> = ({ id, defaultValue, label, type }) => {
  return (
    <fieldset className="mb-[15px] w-full flex flex-col justify-start">
      <label
        className="text-[13px] leading-none mb-2.5  block"
        htmlFor={id}
      >
        {label}
      </label>
      <input
        className="grow shrink-0 rounded px-2.5 text-[15px] leading-none text-violet9 shadow-[0_0_0_1px] shadow-violet9 h-[35px] focus:shadow-[0_0_0_2px] focus:shadow-violet9 outline-none bg-slate-900"
        id={id}
        defaultValue={defaultValue}
        type={type}
      />
    </fieldset>
  );
};

export default Input;
