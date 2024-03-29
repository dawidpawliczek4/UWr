
module LeftistHeap = struct
  type ('a, 'b) heap =
  | HLeaf
  | HNode of int * ('a, 'b) heap * 'a * 'b * ('a, 'b) heap

  let rank = function HLeaf -> 0 | HNode (n, _, _, _, _) -> n

  let heap_ordered p = function
    | HLeaf -> true
    | HNode (_, _, p', _, _) -> p <= p'

  let rec is_valid = function 
    | HLeaf -> true
    | HNode (n, l, p, v, r) -> 
      rank r <= rank l
      && rank r + 1 = n
      && heap_ordered p l
      && heap_ordered p r
      && is_valid l
      && is_valid r

  let make_node p v l r = 
    if rank l >= rank r then
      HNode (rank r + 1, l, p, v, r)
    else
      HNode (rank l + 1, r, p, v, l)
  
end