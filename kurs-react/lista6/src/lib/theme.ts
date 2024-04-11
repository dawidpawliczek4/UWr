import { createTheme } from "@mui/material/styles";
import { red } from "@mui/material/colors";

// A custom theme for this app
const theme = createTheme({
  palette: {
    mode: "dark",
    primary: {
      main: "#a9a9a9",
    },
    secondary: {
      main: "#19857b",
    },
    error: {
      main: red.A400,
    },
    text: {
      primary: "#fff",
    },
    background: {
      default: "rgb(25 27 28)",      
    },
  },

  components: {
    MuiDivider: {
      styleOverrides: {
        root: {
          backgroundColor: "#fff",
        },
      },
    },
    MuiDialog: {
      styleOverrides: {
        paper: {
          backgroundColor: "rgb(0 0 0)",
          // backgroundColor: red[900],
        },        
      },
    },
    MuiTextField: {
      styleOverrides: {
        root: {
          "& .MuiInputBase-input": {
            color: "white", // Text color
          },
          "& .MuiInputLabel-root": {
            color: "white", // Label color when not focused
          },
          // "& .MuiInputLabel-root.Mui-focused": {
          //   color: "white", // Label color when focused
          // },
          "& .MuiOutlinedInput-notchedOutline": {
            borderColor: "white", // Outline color
          },
        },
      },
    },
    MuiMenuItem: {
      styleOverrides: {
        root: {
          color: "white",
          // backgroundColor: "rgb(48 48 48)",
        },
      },
    },
  },
});

export default theme;
