let suffixes xs =
  let rec suffixes' xs acc =
    match xs with
    | [] -> acc
    | _::xs' -> suffixes' xs' (xs::acc)
  in
  suffixes' xs [[]]