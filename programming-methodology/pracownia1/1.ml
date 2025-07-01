let ( let* ) xs ys = List.concat_map ys xs

let rec choose m n =
  if m > n then [] else m :: choose (m+1) n

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

let build_candidate pss n =
  let rec cartesian_product = function
  | [] -> [[]]
  | x::xs ->
    let rest = cartesian_product xs in
    List.concat_map (fun i -> List.map (fun r -> i::r) rest) x
  in
  let all_possible_rows = List.map (fun ps -> build_row ps n) pss in
  cartesian_product all_possible_rows

let verify_row ps xs = 
  let split_into_blocks row =
    let rec aux acc current = function
      | [] -> List.rev (if current != [] then current :: acc else acc)
      | x :: xs ->
        if x then aux acc (x :: current) xs
        else aux (if current != [] then current :: acc else acc) [] xs
    in aux [] [] row
  in 
  let blocks = split_into_blocks xs in
  let block_sizes = List.map List.length blocks in
  block_sizes = ps

let verify_rows pss xss =
  try
    List.for_all2 verify_row pss xss
  with Invalid_argument _ ->
    false

let transpose xss = 
  let rec transpose_aux transposed_matrix = function
    | [] | [] :: _ -> List.rev transposed_matrix
    | matrix ->
      let new_row, remainder_matrix = List.fold_right 
        (fun (head :: tail) (new_row_accumulator, remainder_accumulator) -> 
           (head :: new_row_accumulator, tail :: remainder_accumulator)) 
        matrix ([], []) 
      in
      transpose_aux (new_row :: transposed_matrix) remainder_matrix
  in 
  transpose_aux [] xss


type nonogram_spec = {rows: int list list; cols: int list list}

let solve_nonogram nono =
  build_candidate (nono.rows) (List.length (nono.cols))
  |> List.filter (fun xss -> transpose xss |> verify_rows nono.cols)

let example_1 = {
  rows = [[2];[1];[1]];
  cols = [[1;1];[2]]
}

let example_2 = {
  rows = [[2];[2;1];[1;1];[2]];
  cols = [[2];[2;1];[1;1];[2]]
}

let big_example = {
  rows = [[1;2];[2];[1];[1];[2];[2;4];[2;6];[8];[1;1];[2;2]];
  cols = [[2];[3];[1];[2;1];[5];[4];[1;4;1];[1;5];[2;2];[2;1]]
}