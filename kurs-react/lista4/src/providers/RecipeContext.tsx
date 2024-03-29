import { createContext, useReducer, useState } from "react";

export type RecipeType = {
  id: number;
  name: string;
  description: string;
  favorite: boolean;
};

type RecipeAction = {
  type: string;
  payload: RecipeType;
};

const recipeReducer = (state: RecipeType[], action: RecipeAction) => {
  switch (action.type) {
    case "ADD_EXPENSE":
      return [...state, action.payload];
    case "DELETE_EXPENSE":
      return state.filter((recipe) => recipe.id !== action.payload.id);
    case "CHANGE_FAVORITE":
      return state.map((recipe) =>
        recipe.id === action.payload.id
          ? { ...recipe, favorite: !recipe.favorite }
          : recipe
      );
    default:
      return state;
  }
};

export const RecipeContext = createContext<{
  recipes: RecipeType[];
  addRecipe: (name: string, description: string) => void;
  deleteRecipe: (recipe: RecipeType) => void;
  changeFavorite: (recipe: RecipeType) => void;
  searchString: string;
  setSearchString: (searchString: string) => void;
  favorites: boolean;
  setFavorites: (favorites: boolean) => void;
}>({
  recipes: [],
  addRecipe: () => {},
  deleteRecipe: () => {},
  changeFavorite: () => {},
  searchString: "",
  setSearchString: () => {},
  favorites: false,
  setFavorites: () => {},
});

const initialState: RecipeType[] = [
  {
    id: 1,
    name: "Pizza",
    description: "Delicious pizza",
    favorite: false,
  },
  {
    id: 2,
    name: "Pasta",
    description: "Delicious pasta with tomato sauce and cheese. To cook it, boil the pasta for 10 minutes, then add the sauce and cheese. Enjoy!",
    favorite: false,
  },
];

export const RecipeProvider = ({ children }: { children: React.ReactNode }) => {
  const [recipes, dispatch] = useReducer(recipeReducer, initialState);
  const [searchString, setSearchString] = useState("");
  const [favorites, setFavorites] = useState(false);

  const addRecipe = (name: string, description: string) => {
    const id = Math.max(...recipes.map((recipe) => recipe.id)) + 1;
    const recipe = {
      id: id,
      name,
      description,
      favorite: false,
    };
    dispatch({ type: "ADD_EXPENSE", payload: recipe });
  };

  const deleteRecipe = (recipe: RecipeType) => {
    dispatch({ type: "DELETE_EXPENSE", payload: recipe });
  };

  const changeFavorite = (recipe: RecipeType) => {
    dispatch({ type: "CHANGE_FAVORITE", payload: recipe });
  };

  return (
    <RecipeContext.Provider
      value={{
        recipes,
        addRecipe,
        deleteRecipe,
        changeFavorite,
        searchString,
        setSearchString,
        favorites,
        setFavorites,
      }}
    >
      {children}
    </RecipeContext.Provider>
  );
};
