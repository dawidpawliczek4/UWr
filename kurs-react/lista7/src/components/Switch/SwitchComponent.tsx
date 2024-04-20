import * as Switch from "@radix-ui/react-switch";

interface SwitchComponentProps {
  label: string;
  id: string;
}

const SwitchComponent: React.FC<SwitchComponentProps> = ({ label, id }) => {
  return (
    <fieldset className="mb-[15px] w-full flex flex-col justify-start">
      <label
        className="text-[13px] leading-none mb-2.5  block"
        htmlFor={id}
      >
        {label}
      </label>
      <Switch.Root
        className="w-[42px] h-[25px] bg-mauve11/50 rounded-full relative shadow-[0_2px_10px] shadow-blackA4 focus:shadow-[0_0_0_2px] focus:shadow-black data-[state=checked]:bg-violet9 outline-none cursor-default"
        id={id}
      >
        <Switch.Thumb className="block w-[21px] h-[21px] bg-white rounded-full shadow-[0_2px_2px] shadow-blackA4 transition-transform duration-100 translate-x-0.5 will-change-transform data-[state=checked]:translate-x-[19px]" />
      </Switch.Root>
    </fieldset>
  );
};

export default SwitchComponent;
