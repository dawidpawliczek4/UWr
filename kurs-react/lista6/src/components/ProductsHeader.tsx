import React from "react";
import SortSpan from "./SortSpan";
import { Grid } from "@mui/material";

interface ProductsHeaderProps {}

const ProductsHeader: React.FC<ProductsHeaderProps> = ({}) => {
  return (
    <Grid
      container
      direction="row"
      justifyContent="space-between"
      alignItems="center"
      sx={{
        padding: "1rem",
      }}
    >
      <SortSpan xs={2} id="name">
        Nazwa
      </SortSpan>
      <SortSpan xs={2} id="type">
        Typ
      </SortSpan>
      <SortSpan xs={2} id="price">
        Cena    
      </SortSpan>
      <SortSpan xs={2} id="availability">
        Dostępność
      </SortSpan>
      <SortSpan xs={2} id="quantity">
        Ilość
      </SortSpan>
      <Grid item xs={1}>
        <span>Akcje</span>
      </Grid>
    </Grid>
  );
};

export default ProductsHeader;
