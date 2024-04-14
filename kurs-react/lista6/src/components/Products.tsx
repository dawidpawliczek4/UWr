import React from "react";
import { List, TablePagination } from "@mui/material";
import useProduct from "../providers/useProduct";
import Product from "./Product";
import ProductsHeader from "./ProductsHeader";

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
      <ProductsHeader />
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
