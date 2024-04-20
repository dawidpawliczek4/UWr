import * as Select from "@radix-ui/react-select";
import { ChevronDownIcon, ChevronUpIcon } from "@radix-ui/react-icons";

interface SelectProps {
  label: string;
  children: React.ReactNode;
}

const SelectComponent: React.FC<SelectProps> = ({ label, children }) => {
  return (
    <fieldset className="mb-[15px] w-full flex flex-col justify-start">
      <label className="text-[13px] leading-none mb-2.5  block">{label}</label>
      <Select.Root defaultValue="all">
        <Select.Trigger className="inline-flex items-center justify-center rounded px-[15px] text-[13px] font-semibold leading-none h-[35px] gap-[5px] bg-slate-900 text-violet9 shadow-[0_2px_10px] shadow-black/10 border-violet9 border-[1px]  data-[placeholder]:text-violet9 outline-none">
          <Select.Value />
          <Select.Icon className="text-violet8">
            <ChevronDownIcon />
          </Select.Icon>
        </Select.Trigger>
        <Select.Portal>
          <Select.Content className="overflow-hidden bg-slate-900 rounded-md shadow-[0px_10px_38px_-10px_rgba(22,_23,_24,_0.35),0px_10px_20px_-15px_rgba(22,_23,_24,_0.2)]">
            <Select.ScrollUpButton className="flex items-center justify-center h-[25px] bg-white text-violet8 cursor-default">
              <ChevronUpIcon />
            </Select.ScrollUpButton>
            <Select.Viewport className="p-[5px]">
              <Select.Group>{children}</Select.Group>
            </Select.Viewport>
          </Select.Content>
        </Select.Portal>
      </Select.Root>
    </fieldset>
  );
};

export default SelectComponent;
