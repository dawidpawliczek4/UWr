let rec merge cmp xs ys = 
  match xs, ys with
    | x::xs', y::ys' -> if cmp x y then x :: merge cmp xs' ys else y :: merge cmp xs ys'
    | x, [] -> x
    | [], y -> y

let rec merge_tail cmp xs ys acc =
  match xs, ys with
  | x, [] -> List.rev_append acc x
  | [], y -> List.rev_append acc y
  | x::xs', y::ys' -> if cmp x y then merge_tail cmp xs' ys (x :: acc) else merge_tail cmp xs ys' (y :: acc)

  let halve lst =
    let rec aux slow fast acc =
      match fast with
      | [] | [_] -> (List.rev acc, slow)
      | _::fast'::fast'' -> aux (List.tl slow) fast'' (List.hd slow :: acc)
    in
    aux lst lst []
      

let rec mergesort xs =
  match xs with
  | [x] -> [x]
  | xs ->
 let (fh, sh) = halve xs in
 merge (<=) (mergesort fh) (mergesort sh)