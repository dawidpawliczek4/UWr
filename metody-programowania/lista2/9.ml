(* Funkcja split dzieli listę na dwie części różniące się długością o co najwyżej 1 *)
let split xs =
  let rec aux left right = function
    | [] -> (left, right)
    | [x] -> (x :: left, right)
    | x :: y :: tail -> aux (x :: left) (y :: right) tail
  in aux [] [] xs

(* Funkcja merge łączy dwie posortowane listy w jedną posortowaną listę *)
let rec merge xs ys = match (xs, ys) with
  | ([], _) -> ys
  | (_, []) -> xs
  | (x :: xs', y :: ys') ->
    if x <= y
    then x :: merge xs' ys
    else y :: merge xs ys'

(* Funkcja merge_sort sortuje listę algorytmem sortowania przez złączanie *)
let rec merge_sort = function
  | [] -> []
  | [x] -> [x]
  | xs ->
    let (left, right) = split xs in
    merge (merge_sort left) (merge_sort right)

(* Testowanie funkcji *)
let () =
  let test_list = [8; 2; 4; 7; 4; 2; 1] in
  let (left, right) = split test_list in
  Printf.printf "Split: (%s, %s)\n" (String.concat "; " (List.map string_of_int left)) (String.concat "; " (List.map string_of_int right));
  
  let sorted_list = merge_sort test_list in
  Printf.printf "Sorted: %s\n" (String.concat "; " (List.map string_of_int sorted_list))
