import * as Tabs from "@radix-ui/react-tabs";
import AccountTab from "./components/AccountTab";
import PasswordTab from "./components/PasswordTab";
import PreferencesTab from "./components/PreferencesTab";
import Header from "./components/Header";

function App() {
  return (
    <main className="w-full h-screen flex justify-center items-center text-mauve11">
      <Tabs.Root
        className="flex flex-col w-[400px] shadow-[0_2px_10px] bg-slate-900 shadow-white text-white "
        defaultValue="tab1"
      >
        <Header />

        <Tabs.Content
          className="grow p-5 bg-slate-900 rounded-b-md outline-none "
          value="tab1"
        >
          <AccountTab />
        </Tabs.Content>
        <Tabs.Content
          className="grow p-5 bg-slate-900 rounded-b-md outline-none"
          value="tab2"
        >
          <PasswordTab />
        </Tabs.Content>
        <Tabs.Content
          className="grow p-5 bg-slate-900 rounded-b-md outline-none"
          value="tab3"
        >
          <PreferencesTab />
        </Tabs.Content>
      </Tabs.Root>
    </main>
  );
}

export default App;
