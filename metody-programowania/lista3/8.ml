type 'a tree = 
  |Leaf
  | Node of 'a tree * 'a * 'a tree

(* Modyfikujemy funkcję insert_bst, aby akceptowała duplikaty,
   które będą dodawane do prawego poddrzewa *)
let rec insert_bst x t =
  match t with
  | Leaf -> Node (Leaf, x, Leaf)
  | Node (l, v, r) ->
      if x > v then Node (l, v, insert_bst x r)
      else Node (insert_bst x l, v, r)  (* Zmiana tutaj: Duplikaty idą do lewego poddrzewa *)

(* Funkcja budująca drzewo BST z listy *)
let build_bst xs = List.fold_left (fun acc x -> insert_bst x acc) Leaf xs

(* Funkcja pomocnicza spłaszczająca drzewo BST do listy w kolejności infiksowej,
   używając akumulatora dla efektywności *)
let rec flatten_aux t acc =
  match t with
  | Leaf -> acc
  | Node (l, v, r) -> flatten_aux l (v :: flatten_aux r acc)

(* Funkcja spłaszczająca drzewo BST do listy w kolejności infiksowej *)
let flatten t = flatten_aux t []

(* Funkcja tree_sort, która posortuje listę xs za pomocą drzewa BST *)
let tree_sort xs =
  let bst = build_bst xs in
  flatten bst

(* Przykładowe użycie *)
let unsorted_list = [3; 1; 4; 1; 5; 9; 2; 6; 5; 3; 5]
let sorted_list = tree_sort unsorted_list