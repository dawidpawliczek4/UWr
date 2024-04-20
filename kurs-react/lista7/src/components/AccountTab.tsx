import Input from "./Input/Input";
import SaveButton from "./SaveButton/SaveButton";
import RadioGroupItem from "./RadioGroup/RadioGroupItem";
import RadioGroupComponent from "./RadioGroup/RadioGroupComponent";

interface AccountTabProps {}

const AccountTab: React.FC<AccountTabProps> = ({}) => {
  return (
    <>
      <p className="mb-5 text-mauve11 text-[15px] leading-normal">
        Make changes to your account here. Click save when you're done.
      </p>
      
      <Input id="name" defaultValue="Dawid Pawliczek" label="Name" />
      <Input id="username" defaultValue="@dawidpawliczek" label="Username" />

      <RadioGroupComponent label="Gender">
        <RadioGroupItem value="Male" id="r1" />
        <RadioGroupItem value="Female" id="r2" />
        <RadioGroupItem value="Other" id="r3" />
      </RadioGroupComponent>

      <div className="flex justify-end mt-5">
        <SaveButton>Save changes</SaveButton>
      </div>
    </>
  );
};

export default AccountTab;
