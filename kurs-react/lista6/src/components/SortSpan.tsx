import { Grid } from "@mui/material";
import React from "react";
import { SortBy } from "../lib/types";
import useProduct from "../providers/useProduct";
import ArrowDropUpIcon from '@mui/icons-material/ArrowDropUp';
import ArrowDropDownIcon from '@mui/icons-material/ArrowDropDown';

interface SortSpanProps {
  xs: number;
  children: React.ReactNode;
  id: SortBy;
}

const SortSpan: React.FC<SortSpanProps> = ({ xs, children, id }) => {
  const { sortBy, setSortBy, reverseSort, setReverseSort } = useProduct();

  const handleClick = () => {
    if (id === sortBy && reverseSort) {
      setSortBy("none");
    } else if (id === sortBy && !reverseSort) {
      setReverseSort(true);
    } else {
      setSortBy(id);
      setReverseSort(false);
    }
  };

  return (
    <Grid item xs={xs}>
      <span
        style={{
          cursor: "pointer",                  
        }}
        onClick={handleClick}
      >
        {children}
        {id === sortBy && !reverseSort && <ArrowDropUpIcon sx={{
          fontSize: "1rem",
        }} />}
        {id === sortBy && reverseSort && <ArrowDropDownIcon sx={{
          fontSize: "1rem",        
        }} />}                
      </span>
    </Grid>
  );
};

export default SortSpan;
