import React from "react";
import { Divider, Grid } from "@mui/material";
import { ProductType } from "../lib/types";
import DeleteIcon from "@mui/icons-material/Delete";
import useProduct from "../providers/useProduct";
import Button from "@mui/material/Button";
import Dialog from "@mui/material/Dialog";
import DialogActions from "@mui/material/DialogActions";
import DialogTitle from "@mui/material/DialogTitle";

interface ProductProps {
  product: ProductType;
}

const Product: React.FC<ProductProps> = ({ product }) => {
  const { setProducts } = useProduct();
  const [open, setOpen] = React.useState(false);
  const handleDeleteProduct = () => {
    setProducts((prev) => prev.filter((p) => p.id !== product.id));
    setOpen(false);    
  };
  return (
    <div key={product.id}>
      <Grid
        container
        direction="row"
        justifyContent="space-between"
        alignItems="center"
        sx={{
          padding: "1rem",
        }}
      >
        <Grid item xs={2}>
          {product.name}
        </Grid>
        <Grid item xs={2}>
          {product.type}
        </Grid>
        <Grid item xs={2}>
          {product.price}
        </Grid>
        <Grid item xs={2}>
          {product.availability ? "Tak" : "Nie"}
        </Grid>
        <Grid item xs={2}>
          {product.quantity}
        </Grid>
        <Grid item xs={1}>
          <DeleteIcon
            sx={{ cursor: "pointer", color: "red" }}
            onClick={() => setOpen(true)}
          />
        </Grid>
      </Grid>
      <Divider />

      <Dialog
        open={open}
        onClose={() => setOpen(false)}
        aria-labelledby="alert-dialog-title"
        aria-describedby="alert-dialog-description"
      >
        <DialogTitle id="alert-dialog-title">{"Are you sure?"}</DialogTitle>
        <DialogActions>
          <Button onClick={handleDeleteProduct}>YES</Button>
          <Button onClick={() => setOpen(false)} autoFocus>
            NO
          </Button>
        </DialogActions>
      </Dialog>
    </div>
  );
};

export default Product;
