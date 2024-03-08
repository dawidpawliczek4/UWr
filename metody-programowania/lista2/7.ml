let rec is_sorted xs =
  match xs with
  | [] -> true
  | [x] -> true
  | x::y::xs' -> x <= y && is_sorted (y::xs')