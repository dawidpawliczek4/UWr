import * as Slider from "@radix-ui/react-slider";

interface SliderComponentProps {
  label: string;
}

const SliderComponent: React.FC<SliderComponentProps> = ({ label }) => {
  return (
    <fieldset className="mb-[15px] w-full flex flex-col justify-start">
      <label
        className="text-[13px] leading-none mb-2.5 text-white block"
        htmlFor="notifications"
      >
        {label}
      </label>
      <Slider.Root
        className="relative flex items-center select-none touch-none w-full h-5"
        defaultValue={[50]}
        max={100}
        step={1}
      >
        <Slider.Track className="bg-mauve11 relative grow rounded-full h-[3px]">
          <Slider.Range className="absolute bg-violet9 rounded-full h-full" />
        </Slider.Track>
        <Slider.Thumb
          className="block w-5 h-5 bg-white shadow-[0_2px_10px] shadow-blackA4 rounded-[10px] hover:bg-violet3 focus:outline-none "
          aria-label="Volume"
        />
      </Slider.Root>
    </fieldset>
  );
};

export default SliderComponent;
