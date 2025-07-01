let select xs =
  let rec select_aux min rest = function
    | [] -> (min, rest)
    | h::t ->
      if h < min
      then select_aux h (min::rest) t
      else select_aux min (h::rest) t
  in
  match xs with
  | [] -> (neg_infinity, [])
  | h::t -> select_aux h [] t

let rec select_sort xs =
  match xs with
  | [] -> []
  | _ -> 
    let (min, rest) = select xs in
    min :: select_sort rest

