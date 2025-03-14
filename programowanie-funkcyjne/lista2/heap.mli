module LeftistHeap : sig
    type 'a t
    type 'a view = 
    | Leaf
    | Node of 'a * int *  'a t * 'a t
    
    val empty : 'a t
    val insert : 'a -> 'a t -> 'a t
    val find_min : 'a t -> int
    val delete_min : 'a t -> 'a t
    val merge : 'a t -> 'a t -> 'a t

    val view: 'a t -> 'a view
end