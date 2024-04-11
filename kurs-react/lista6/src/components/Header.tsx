import { Avatar, Grid } from "@mui/material";
import React from "react";

interface HeaderProps {}

const Header: React.FC<HeaderProps> = ({}) => {
  return (
    <Grid
      container
      direction="row"
      justifyContent="space-between"
      alignItems="center"
      sx={{
        padding: "1rem",
        position: "fixed",
        backgroundColor: "rgb(35 37 39)",
        height: "4rem",      
        zIndex: 1000,          
      }}
    >
      <Grid
        item
        sx={{
          color: "white",
          fontSize: "1.7rem",
        }}
      >
        Sklep
      </Grid>
      <Grid item>
        <Avatar />
      </Grid>
    </Grid>
  );
};

export default Header;
