import React from "react";
import Input from "./Input/Input";
import SaveButton from "./SaveButton/SaveButton";

interface PasswordTabProps {}

const PasswordTab: React.FC<PasswordTabProps> = ({}) => {
  return (
    <>
      <p className="mb-5 text-mauve11 text-[15px] leading-normal">
        Change your password here. After saving, you'll be logged out.
      </p>

      <Input id="current-password" label="Current password" type="password" />
      <Input id="new-password" label="New password" type="password" />
      <Input id="confirm-password" label="Confirm password" type="password" />
      
      <div className="flex justify-end mt-5">
        <SaveButton>Change password</SaveButton>
      </div>
    </>
  );
};

export default PasswordTab;
