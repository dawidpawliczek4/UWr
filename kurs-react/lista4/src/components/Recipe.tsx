import { RecipeType } from "../providers/RecipeContext";
import useRecipe from "../providers/useRecipe";
import { MdFavorite } from "react-icons/md";
import { FaTrashAlt } from "react-icons/fa";

const Recipe = ({ recipe }: { recipe: RecipeType }) => {
  const { deleteRecipe, changeFavorite } = useRecipe();
  return (
    <li key={recipe.id} className="flex justify-between items-center mb-2">
      <div>
        <h2 className={`font-bold ${recipe.favorite ? "text-green-500" : ""}`}>
          {recipe.name}
        </h2>
        <p>{recipe.description}</p>
      </div>
      <div className="flex gap-x-4 pl-2">
        <FaTrashAlt
        className="text-red-500 text-xl cursor-pointer"
          onClick={() => {
            deleteRecipe(recipe);
          }}
        />
        <MdFavorite
          className={`${recipe.favorite ? "text-green-500" : ""} text-xl cursor-pointer`}
          onClick={() => {
            changeFavorite(recipe);
          }}
        />
      </div>
    </li>
  );
};

export default Recipe;