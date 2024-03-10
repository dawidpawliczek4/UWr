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


let tree_product t = 
  fold_tree (fun l v r -> l * v * r) 1 t

let tree_flip t =
  fold_tree (fun l v r -> Node (r, v, l)) Leaf t

let tree_height t =
  fold_tree (fun l v r -> 1 + max l r) 0 t

let tree_span t =
  let f l v r = match (l, r) with
    | (None, None) -> Some (v, v)  (* Jeśli oba poddrzewa są puste, zwracamy wartość tego węzła jako min i max. *)
    | (Some (lmin, lmax), None) -> Some (min lmin v, max lmax v)  (* Jeśli istnieje tylko lewe poddrzewo *)
    | (None, Some (rmin, rmax)) -> Some (min rmin v, max rmax v)  (* Jeśli istnieje tylko prawe poddrzewo *)
    | (Some (lmin, lmax), Some (rmin, rmax)) -> Some (min lmin (min rmin v), max lmax (max rmax v))  (* Jeśli istnieją oba poddrzewa *)
  in
  fold_tree f None t

let rec preorder t =
  match t with
  | Leaf -> []
  | Node (l, v, r) -> [v] @ (preorder l) @ (preorder r)