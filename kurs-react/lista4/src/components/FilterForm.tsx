import useRecipe from "../providers/useRecipe";
import Input from "./Input";

const FilterForm = () => {
  const { setFavorites, favorites, searchString, setSearchString } =
    useRecipe();

  return (    
        <div className="py-4 gap-x-2 flex justify-center">
          <Input            
            placeholder="Search"
            value={searchString}
            onChange={(e) => {
              setSearchString(e.target.value);
            }}
            className="w-1/2"
          />
          <label className="bg-blue-500 p-2 self-start rounded-lg text-white cursor-pointer">
            Favorites
            <input
              type="checkbox"
              className="mx-2 w-4 h-4 accent-green-500"
              onChange={(e) => setFavorites(e.target.checked)}
              checked={favorites}
            />
          </label>
        </div>      
  );
};

export default FilterForm;
