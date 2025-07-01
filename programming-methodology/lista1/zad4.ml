let suma a b c =
  let max1, max2 = 
    if a > b then
      if b > c then a, b
      else if a > c then a, c
      else c, a
    else
      if a > c then b, a
      else if b > c then b, c
      else c, b
  in
  max1 * max1 + max2 * max2;;