let rec choose m n =
  if m > n then [] else m :: choose (m+1) n

let two_num_product n m =
  List.concat_map 
  (fun a -> List.concat_map (fun b -> if a * b = m then [a, b] else []) (choose a n))
  (choose 1 n)

let ( let* ) xs ys = List.concat_map ys xs

let two_num_product n m =
  let* a = choose 1 n in
  let* b = choose a n in
  if a * b = m then [a, b] else []

let pairs = 
  let* a = [1; 2; 3] in
  let* b = [4; 5; 6] in
  [a, b]