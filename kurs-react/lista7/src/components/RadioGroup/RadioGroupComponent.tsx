import * as RadioGroup from "@radix-ui/react-radio-group";

interface RadioGroupComponentProps {
  label: string;
  children: React.ReactNode;
}

const RadioGroupComponent: React.FC<RadioGroupComponentProps> = ({
  label,
  children,
}) => {
  return (
    <fieldset className="mb-[15px] w-full flex flex-col justify-start">
      <label className="text-[13px] leading-none mb-2.5 block">
        {label}
      </label>
      <RadioGroup.Root
        className="flex flex-col gap-2.5"
        aria-label="View density"
      >
        {children}
      </RadioGroup.Root>
    </fieldset>
  );
};

export default RadioGroupComponent;
