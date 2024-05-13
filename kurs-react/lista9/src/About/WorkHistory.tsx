import React from "react";
import * as Tabs from "@radix-ui/react-tabs";

interface WorkHistoryProps {}

const WorkHistory: React.FC<WorkHistoryProps> = ({}) => {
  return (
    <Tabs.Root
      className="flex flex-row gap-x-2 mt-12 w-2/3 h-[300px]"
      defaultValue="tab1"
    >
      <Tabs.List className="flex flex-col items-start w-[400px] ">
        <Tabs.Trigger
          className="data-[state=active]:text-violet-700 border-l-[1px] border-violet-700/60 data-[state=active]:border-violet-700 p-2 "
          value="tab1"
        >
          Google
        </Tabs.Trigger>
        <Tabs.Trigger
          className="data-[state=active]:text-violet-700 border-l-[1px] border-violet-700/60 data-[state=active]:border-violet-700 p-2 "
          value="tab2"
        >
          Microsoft
        </Tabs.Trigger>
        <Tabs.Trigger
          className="data-[state=active]:text-violet-700 border-l-[1px] border-violet-700/60 data-[state=active]:border-violet-700 p-2 "
          value="tab3"
        >
          Meta
        </Tabs.Trigger>
        <Tabs.Trigger
          className="data-[state=active]:text-violet-700 border-l-[1px] border-violet-700/60 data-[state=active]:border-violet-700 p-2 "
          value="tab4"
        >
          Goldman Sachs
        </Tabs.Trigger>
      </Tabs.List>
      <Tabs.Content value="tab1">
        I worked at google as a software engineer. I worked on the search
        engine. I was really happy to work there. I learned a lot of things. I
        worked on the search engine.
      </Tabs.Content>
      <Tabs.Content value="tab2">
        I worked at Microsoft as a software engineer. I worked on the search
        engine. I was really happy to work there. I learned a lot of things. I
        worked on the search engine.
      </Tabs.Content>
      <Tabs.Content value="tab3">
        I worked at Meta as a software engineer. I worked on the search engine. I
        was really happy to work there. I learned a lot of things. I worked on
        the search engine.
      </Tabs.Content>
      <Tabs.Content value="tab4">
        I worked at Goldman Sachs as a software engineer. I worked on the search
        engine. I was really happy to work there. I learned a lot of things. I
        worked on the search engine.
      </Tabs.Content>
    </Tabs.Root>
  );
};

export default WorkHistory;
