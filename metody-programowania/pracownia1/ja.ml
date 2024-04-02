let ( let* ) xs ys = List.concat_map ys xs

let rec choose m n =
  if m > n then [] else m :: choose (m+1) n

let two_num_product n m =
  List.concat_map 
  (fun a -> List.concat_map (fun b -> if a * b = m then [a, b] else []) (choose a n))
  (choose 1 n)

let two_num_product n m =
  let* a = choose 1 n in
  let* b = choose a n in
  if a * b = m then [a, b] else []

let rec build_row spec len =   
  match spec with
| [] -> [List.init len (fun _ -> false)]
| [x] ->     
  List.init (max 0 (len - x + 1)) (fun i ->
    (List.init i (fun _ -> false)) @ (List.init x (fun _ -> true)) @ (List.init (len - x - i) (fun _ -> false))
  )
| x:: xs ->
    List.concat_map (fun i ->
      let first_part = (List.init i (fun _ -> false)) @ (List.init x (fun _ -> true)) in
      let rest_len = max 0 (len - x - i - 1) in
      List.map (fun rest -> first_part @ [false] @ rest) (build_row xs rest_len)
    ) (List.init (len - x - List.length spec + 2) (fun i -> i))