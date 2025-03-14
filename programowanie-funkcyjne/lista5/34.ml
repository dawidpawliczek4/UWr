type 'a lazytree = 
  | Node of (('a lazytree) Lazy.t) * 'a * (('a lazytree) Lazy.t)


let rec create_tree (a, b) (c, d) =
  let node = (a+c, b+d) in
  Node(
    lazy (create_tree (a, b) (a+c, b+d)),
      node,
    lazy (create_tree (a+c, b+d) (c, d))
  )

let all_trees = create_tree (0,1) (1,0)

let get_left_subtree lt = 
  match lt with
  | Node (l, v, r) -> l


let get_right_subtree lt = 
  match lt with
  | Node (l, v, r) -> r

  
let lazy_cons x xs = 
  fun () -> Seq.Cons (x, xs ())

let rec bfs = function Node(l,v,r) ->
  lazy_cons v (fun () -> Seq.interleave (bfs (Lazy.force l)) (bfs (Lazy.force r)) )

let rec take n seq =
  if n = 0 then []
  else match seq () with
    | Seq.Nil -> []
    | Seq.Cons (x, xs) -> x :: take (n - 1) xs

let all_positive_rationals = bfs (create_tree (0, 1) (1, 0))

let first_10_rationals = take 10 all_positive_rationals