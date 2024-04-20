import { LegacyRef, forwardRef } from "react";
import classnames from "classnames";
import * as Select from "@radix-ui/react-select";
import { CheckIcon } from "@radix-ui/react-icons";

type SelectItemProps = {
  children: React.ReactNode;
  className?: string;
  value: string;
};

const SelectItem = forwardRef<HTMLLIElement, SelectItemProps>(
  ({ children, className, ...props }, forwardedRef) => {
    return (
      <Select.Item
        className={classnames(
          "text-[13px] leading-none text-violet9 rounded-[3px] flex items-center h-[25px] pr-[35px] pl-[25px] relative select-none data-[disabled]:text-mauve8 data-[disabled]:pointer-events-none data-[highlighted]:outline-none data-[highlighted]:bg-violet9 data-[highlighted]:text-violet1",
          className
        )}
        {...props}
        ref={forwardedRef as LegacyRef<HTMLDivElement>}
      >
        <Select.ItemText>{children}</Select.ItemText>
        <Select.ItemIndicator className="absolute left-0 w-[25px] inline-flex items-center justify-center">
          <CheckIcon />
        </Select.ItemIndicator>
      </Select.Item>
    );
  }
);

export default SelectItem;
