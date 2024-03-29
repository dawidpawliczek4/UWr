import FilterForm from "./components/FilterForm";
import Recipe from "./components/Recipe";
import RecipeForm from "./components/RecipeForm";
import useRecipe from "./providers/useRecipe";


function App() {
  const { recipes, favorites, searchString } = useRecipe();

  const filteredRecipes = recipes.filter((recipe) => {
    if (favorites && !recipe.favorite) {
      return false;
    }

    const wholeString = recipe.name + " " + recipe.description;

    if (
      searchString &&
      !wholeString.toLowerCase().includes(searchString.toLowerCase())
    ) {
      return false;
    }

    return true;
  });

  return (
    <div className="flex justify-center items-center pt-20">
      <div className="w-1/2">
        <h1 className="text-2xl font-bold mb-4">Recipes</h1>
        <RecipeForm />
        <FilterForm />
        <ul>
          {filteredRecipes.map((recipe) => (
            <Recipe recipe={recipe} />
          ))}
        </ul>
      </div>
    </div>
  );
}

export default App;
