import React from "react";
import {
  Fab,
  Dialog,
  DialogTitle,
  DialogActions,
  Button,
  TextField,
  Grid,
  MenuItem,
} from "@mui/material";
import AddIcon from "@mui/icons-material/Add";
import useProduct from "../providers/useProduct";

interface AddProductProps {}

const AddProduct: React.FC<AddProductProps> = ({}) => {
  const { setProducts } = useProduct();
  const [open, setOpen] = React.useState(false);
  const [name, setName] = React.useState<string>();
  const [type, setType] = React.useState<number>();
  const [price, setPrice] = React.useState<number>();
  const [quantity, setQuantity] = React.useState<number>();

  const handleAddProduct = () => {
    if (!name || !type || !price || !quantity) {
      return;
    }
    setProducts((prev) => {
      const maxId = Math.max(...prev.map((p) => p.id));
      return [
        ...prev,
        {
          id: maxId,
          name: name,
          type: type,
          price: price,
          availability: true,
          quantity: quantity,
        },
      ];
    });
    setName("");
    setType(undefined);
    setPrice(undefined);
    setQuantity(undefined);
    setOpen(false);
  };

  return (
    <>
      <Fab
        color="secondary"
        variant="circular"
        aria-label="add"
        onClick={() => setOpen(true)}
        // disabled={open}
        sx={{
          position: "fixed",
          bottom: "1rem",
          right: "1rem",
        }}
      >
        <AddIcon />
      </Fab>

      <Dialog
        open={open}
        onClose={() => setOpen(false)}
        sx={{
          padding: "24px",
        }}
      >
        <DialogTitle id="alert-dialog-title">
          {"Dodaj nowy produkt"}
        </DialogTitle>
        <Grid
          container
          spacing={2}
          sx={{
            padding: "24px",
          }}
        >
          <Grid item xs={4}>
            <TextField
              id="name"
              label="Nazwa"
              variant="outlined"
              type="text"
              value={name}
              onChange={(e) => setName(e.target.value)}
              required
            />
          </Grid>
          <Grid item xs={4}>
            <TextField
              id="typ"
              label="Typ"
              variant="outlined"
              value={type}
              onChange={(e) => setType(Number(e.target.value))}
              select
              fullWidth
              required
            >
              <MenuItem value={1}>Pierwszy</MenuItem>
              <MenuItem value={2}>Drugi</MenuItem>
              <MenuItem value={3}>Trzeci</MenuItem>
            </TextField>
          </Grid>
          <Grid item xs={4}>
            <TextField
              id="price"
              label="Cena"
              variant="outlined"
              type="number"
              value={price}
              onChange={(e) => setPrice(Number(e.target.value))}
              required
            />
          </Grid>
          <Grid item xs={4}>
            <TextField
              id="quantity"
              label="Ilość"
              variant="outlined"
              type="number"
              value={quantity}
              onChange={(e) => setQuantity(Number(e.target.value))}
              required
            />
          </Grid>
        </Grid>
        <DialogActions>
          <Button onClick={() => setOpen(false)}>Anuluj</Button>
          <Button onClick={() => handleAddProduct()} autoFocus>
            Dodaj
          </Button>
        </DialogActions>
      </Dialog>
    </>
  );
};

export default AddProduct;
