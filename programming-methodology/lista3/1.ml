let fold_left f a xs =
  let rec it xs acc =
    match xs with
    | [] -> acc
    | x :: xs' -> it xs' (f acc x)
  in it xs a

let product xs = 
  match xs with
  | [] -> 0
  | _ -> fold_left (fun x y -> x * y) 1 xs