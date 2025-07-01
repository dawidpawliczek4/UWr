let maximum xs =
  let rec max xs m = 
    match xs with
    | [] -> m
    | x::xs -> if x > m then max xs x else max xs m
  in max xs neg_infinity