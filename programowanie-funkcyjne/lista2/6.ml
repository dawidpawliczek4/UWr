let rec insert x lst = 
  match lst with
  | [] -> [[x]]
  | h::t -> (x::lst) :: (List.map (fun el -> h::el) (insert x t))
  

let rec perm lst = 
  match lst with
  | [] -> [[]]
  | h :: t ->
    List.flatten (List.map (insert h) (perm t))


let lst = [1;2;3]