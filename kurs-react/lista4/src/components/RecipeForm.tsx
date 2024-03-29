import { useState } from "react";
import useRecipe from "../providers/useRecipe";
import Input from "./Input";

const RecipeForm = () => {
  const { addRecipe } = useRecipe();
  const [name, setName] = useState("");
  const [description, setDescription] = useState("");

  const handleSubmit = (e: React.FormEvent<HTMLFormElement>) => {
    e.preventDefault();
    if (!name || !description) return;
    addRecipe(name, description);
    setName("");
    setDescription("");
  };

  return (
    <form onSubmit={handleSubmit} className="flex flex-row gap-x-2 w-full">
      <Input
        placeholder="Add name here..."
        value={name}
        onChange={(e) => {
          setName(e.target.value);
        }}
      />
      <Input
        placeholder="Add description here..."
        className="flex-grow"
        value={description}
        onChange={(e) => {
          setDescription(e.target.value);
        }}
      />
      <button
        type="submit"
        className="p-2 border-[1px] border-black-300 rounded-lg"
      >
        Add Recipe
      </button>
    </form>
  );
};

export default RecipeForm;
