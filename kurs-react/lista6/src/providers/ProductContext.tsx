import React from "react";
import { createContext, useState } from "react";
import { ProductType } from "../lib/types";
import { SortBy } from "../lib/types";
import { initialProducts } from "../lib/dummy_data";

export const ProductContext = createContext<{
  products: ProductType[];
  setProducts: React.Dispatch<React.SetStateAction<ProductType[]>>;
  sortBy: SortBy;
  setSortBy: React.Dispatch<React.SetStateAction<SortBy>>;
  reverseSort: boolean;
  setReverseSort: React.Dispatch<React.SetStateAction<boolean>>;
}>({
  products: [],
  setProducts: () => {},
  sortBy: "none",
  setSortBy: () => {},
  reverseSort: false,
  setReverseSort: () => {},
});

export const ProductProvider = ({
  children,
}: {
  children: React.ReactNode;
}) => {
  const [products, setProducts] = useState<ProductType[]>(initialProducts);
  const [sortBy, setSortBy] = useState<SortBy>("none");
  const [reverseSort, setReverseSort] = useState<boolean>(false);

  return (
    <ProductContext.Provider
      value={{
        products,
        setProducts,
        sortBy,
        setSortBy,
        reverseSort,
        setReverseSort,
      }}
    >
      {children}
    </ProductContext.Provider>
  );
};
