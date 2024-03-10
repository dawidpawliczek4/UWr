(* A representation of an empty set. It always returns false because it contains no elements. *)
let empty_set _ = false

(* A representation of a singleton set. It returns true if and only if the element is the one in the set. *)
let singleton a x = x = a

(* A function that checks if an element belongs to a set. *)
let in_set x s = s x

(* A union of two sets. It returns true if the element is in either set. *)
let union s t x = (s x) || (t x)

(* An intersection of two sets. It returns true if the element is in both sets. *)
let intersect s t x = (s x) && (t x)