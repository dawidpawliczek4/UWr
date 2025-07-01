type 'a tree =
  | Leaf
  | Node of 'a tree * 'a * 'a tree

let t =
  Node 
  (Node (Leaf, 2, Leaf), 
  5, 
  (Node ((Node (Leaf, 6, Leaf)), 8, (Node (Leaf, 9, Leaf))))
  )

let rec fold_tree f a t =
  match t with
  | Leaf -> a
  | Node (l, v, r) -> f (fold_tree f a l) v (fold_tree f a r)

let flatten_old t = fold_tree (fun l v r -> l @ [v] @ r) [] t

let rec flat_append t xs =  
  match t with
  | Leaf -> xs 
  | Node (l, v, r) -> flat_append l (v :: flat_append r xs)

let flatten t =
  flat_append t []