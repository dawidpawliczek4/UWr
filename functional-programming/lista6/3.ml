exception EarlyExit


let for_all : ('a -> bool) -> 'a list -> bool =
  fun callback list ->
    try
    List.fold_left (fun acc x -> if callback x then true else raise EarlyExit) true list
    with EarlyExit -> false


let mult_list : int list -> int =
  fun list ->
    try
    List.fold_left (fun acc x -> if x = 0 then raise EarlyExit else acc * x) 1 list
    with EarlyExit -> 0

let sorted : int list -> bool =
  fun xs ->
    try
    let _ = List.fold_left (fun acc x -> if acc > x then raise EarlyExit else x) (List.hd xs) xs 
    in true
    with EarlyExit -> false