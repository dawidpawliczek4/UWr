type 'a tree =
  | Leaf
  | Node of 'a tree * 'a * 'a tree

let t =
  Node 
  (Node (Leaf, 20, Leaf), 
  5, 
  (Node ((Node (Leaf, 6, Leaf)), 8, (Node (Leaf, 9, Leaf))))
  )

let rec fold_tree f a t =
  match t with
  | Leaf -> a
  | Node (l, v, r) -> f (fold_tree f a l) v (fold_tree f a r)


let tree_product t = 
  fold_tree (fun l v r -> l * v * r) 1 t

let tree_flip t =
  fold_tree (fun l v r -> Node (r, v, l)) Leaf t

let tree_height t =
  fold_tree (fun l v r -> 1 + max l r) 0 t

let tree_span t = 
let flatten x = fold_tree (fun l v r -> l @ [v] @ r) [] x
in
let flat = flatten t
in match flat with
  | [] -> (0, 0)
  | _ -> (List.hd flat, List.hd (List.rev flat))

let preorder t =
  let f l v r = [v] @ l @ r in
  fold_tree f [] t