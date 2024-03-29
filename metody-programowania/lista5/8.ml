let rec is_sorted = function
  | [] | [_] -> true
  | x :: y :: rest -> x <= y && is_sorted (y :: rest)

let rec insert x = function
  | [] -> [x]
  | y :: rest -> if x <= y then x :: y :: rest else y :: insert x rest


