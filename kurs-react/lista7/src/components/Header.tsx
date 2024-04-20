import * as Tabs from "@radix-ui/react-tabs";

interface HeaderProps {}

const Header: React.FC<HeaderProps> = ({}) => {
  return (
    <Tabs.List
      className="shrink-0 flex border-b border-mauve6 bg-slate-900"
      aria-label="Manage your account"
    >
      <Tabs.Trigger
        className="bg-slate-900 px-5 h-[45px] flex-1 flex items-center justify-center text-[15px] leading-none  select-none first:rounded-tl-md last:rounded-tr-md hover:text-violet9 data-[state=active]:text-violet9 data-[state=active]:shadow-[inset_0_-1px_0_0,0_1px_0_0] data-[state=active]:shadow-current data-[state=active]:focus:relative outline-none cursor-default "
        value="tab1"
      >
        Account
      </Tabs.Trigger>
      <Tabs.Trigger
        className="bg-slate-900 px-5 h-[45px] flex-1 flex items-center justify-center text-[15px] leading-none  select-none first:rounded-tl-md last:rounded-tr-md hover:text-violet9 data-[state=active]:text-violet9 data-[state=active]:shadow-[inset_0_-1px_0_0,0_1px_0_0] data-[state=active]:shadow-current data-[state=active]:focus:relative  outline-none cursor-default"
        value="tab2"
      >
        Password
      </Tabs.Trigger>
      <Tabs.Trigger
        className="bg-slate-900 px-5 h-[45px] flex-1 flex items-center justify-center text-[15px] leading-none  select-none first:rounded-tl-md last:rounded-tr-md hover:text-violet9 data-[state=active]:text-violet9 data-[state=active]:shadow-[inset_0_-1px_0_0,0_1px_0_0] data-[state=active]:shadow-current data-[state=active]:focus:relative  outline-none cursor-default"
        value="tab3"
      >
        Preferences
      </Tabs.Trigger>
    </Tabs.List>
  );
};

export default Header;
