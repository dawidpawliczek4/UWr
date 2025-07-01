module LeftistHeap : sig
  type 'a t
  val empty: 'a t
  val insert : 'a -> 'a t -> 'a t
  val find_min : 'a t -> 'a
  val delete_min : 'a t -> 'a t
  val merge : 'a t -> 'a t -> 'a t
end = struct
  type 'a t = 
  | Node of 'a * int *  'a t * 'a t
  | Leaf
  and 'a view = 'a t

  let rank = function
  | Node (_,rank,_,_) -> rank
  | Leaf -> 0

let make_node v l r =
  let rank_l = rank l in
  let rank_r = rank r in
  if rank_l >= rank_r then
    Node(v, rank_r+1, l, r)
  else
    Node(v,rank_l+1, r, l)

let rec merge t1 t2 =
  match t1, t2 with
  | Leaf, t -> t
  | t, Leaf -> t
  | Node(v1, _, l1, r1), Node(v2, _, l2, r2) ->
    if v1 <= v2 then
      make_node v1 l1 (merge r1 t2)
    else
      make_node v2 l2 (merge t1 r2)
  
let insert v t =
  merge (Node(v, 1, Leaf, Leaf)) t

  let find_min = function
  | Leaf -> failwith "Heap is empty"
  | Node (v,_,_,_) -> v

let delete_min t =
  match t with
  | Leaf -> Leaf
  | Node(v, rank, l, r) ->
    merge l r

    let empty = Leaf
end