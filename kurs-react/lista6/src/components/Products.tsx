import React from "react";
import { List, Grid, TablePagination } from "@mui/material";
import useProduct from "../providers/useProduct";
import Product from "./Product";
import SortSpan from "./SortSpan";

interface ProductsProps {}

const Products: React.FC<ProductsProps> = ({}) => {
  const { products, sortBy, reverseSort } = useProduct();
  const [page, setPage] = React.useState(0);
  const [rowsPerPage, setRowsPerPage] = React.useState(10);

  const handleChangePage = (
    event: React.MouseEvent<HTMLButtonElement> | null,
    newPage: number
  ) => {
    setPage(newPage);
  };

  const handleChangeRowsPerPage = (
    event: React.ChangeEvent<HTMLInputElement | HTMLTextAreaElement>
  ) => {
    setRowsPerPage(parseInt(event.target.value, 10));
    setPage(0);
  };

  let sortedProducts = products;

  if (sortBy !== "none") {
    sortedProducts = [...products].sort((a, b) => {
      if (reverseSort) {
        const temp = a;
        a = b;
        b = temp;
      }
      if (a[sortBy] < b[sortBy]) {
        return -1;
      }
      if (a[sortBy] > b[sortBy]) {
        return 1;
      }
      return 0;
    });
  }

  sortedProducts = sortedProducts.slice(
    page * rowsPerPage,
    page * rowsPerPage + rowsPerPage
  );

  return (
    <div
      style={{
        width: "60%",
        margin: "auto",
      }}
    >
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
      <List>
        {sortedProducts.map((product) => (
          <Product product={product} />
        ))}
      </List>
      <TablePagination
        count={products.length}
        page={page}
        onPageChange={handleChangePage}
        rowsPerPage={rowsPerPage}
        onRowsPerPageChange={handleChangeRowsPerPage}
      />
    </div>
  );
};

export default Products;
