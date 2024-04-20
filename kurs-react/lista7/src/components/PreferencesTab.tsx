import SelectComponent from "./Select/SelectComponent";
import SaveButton from "./SaveButton/SaveButton";
import SelectItem from "./Select/SelectItem";
import SliderComponent from "./Slider/SliderComponent";
import SwitchComponent from "./Switch/SwitchComponent";

interface PreferencesTabProps {}

const PreferencesTab: React.FC<PreferencesTabProps> = ({}) => {
  return (
    <>
      <p className="mb-5 text-mauve11 text-[15px] leading-normal">
        Change preferences here. Click save when you're done.
      </p>

      <SelectComponent label="Notafication Settings">
        <SelectItem value="all">All</SelectItem>
        <SelectItem value="only-f">Only followed</SelectItem>
        <SelectItem value="none">None</SelectItem>
      </SelectComponent>

      <SliderComponent label="Notafication frequency" />

      <SwitchComponent
        label="Collect additional data"
        id="collect-data-switch"
      />
      
      <div className="flex justify-end mt-5">
        <SaveButton>Save preferences</SaveButton>
      </div>
    </>
  );
};

export default PreferencesTab;
