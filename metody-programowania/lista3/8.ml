type 'a tree = 
  |Leaf
  | Node of 'a tree * 'a * 'a tree

let rec insert_bst x t =
  match t with
  | Leaf -> Node (Leaf, x, Leaf)
  | Node (l, v, r) ->
      if x >= v then Node (l, v, insert_bst x r)
      else Node (insert_bst x l, v, r)          

let build_bst xs = List.fold_left (fun acc x -> insert_bst x acc) Leaf xs

let rec flatten_aux t acc =
  match t with
  | Leaf -> acc
  | Node (l, v, r) -> flatten_aux l (v :: flatten_aux r acc)

let flatten t = flatten_aux t []

let tree_sort xs =
  let bst = build_bst xs in
  flatten bst

let unsorted_list = [3; 1; 4; 1; 5; 9; 2; 6; 5; 3; 5]
let sorted_list = tree_sort unsorted_list