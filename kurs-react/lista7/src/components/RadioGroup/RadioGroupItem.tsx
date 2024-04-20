import * as RadioGroup from "@radix-ui/react-radio-group";

interface RadioGroupItemProps {
  id: string;
  value: string;
}

const RadioGroupItem: React.FC<RadioGroupItemProps> = ({ id, value }) => {
  return (
    <div className="flex items-center">
      <RadioGroup.Item
        className="bg-white w-[25px] h-[25px] rounded-full shadow-[0_2px_10px] shadow-blackA4 hover:bg-violet-100  outline-none cursor-default"
        value={value}
        id={id}
      >
        <RadioGroup.Indicator className="flex items-center justify-center w-full h-full relative after:content-[''] after:block after:w-[11px] after:h-[11px] after:rounded-[50%] after:bg-violet11" />
      </RadioGroup.Item>
      <label className=" text-[15px] leading-none pl-[15px]" htmlFor={id}>
        {value}
      </label>
    </div>
  );
};

export default RadioGroupItem;
