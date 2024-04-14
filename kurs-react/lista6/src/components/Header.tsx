import { Avatar, Box, Grid } from "@mui/material";
import React from "react";

interface HeaderProps {}

const Header: React.FC<HeaderProps> = ({}) => {
  const [showName, setShowName] = React.useState(false);

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
        <Avatar
        alt="Your Name"
          onMouseEnter={() => setShowName(true)}
          onMouseLeave={() => setShowName(false)}
        />
        {showName && (
          <Box
            sx={{
              position: "absolute",
              marginRight: "1rem",
              marginTop: "1rem",
              textAlign: "center",
            }}
          >
            Your Name
          </Box>
        )}
      </Grid>
    </Grid>
  );
};

export default Header;
