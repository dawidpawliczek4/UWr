type ('a, 'b) format = (string -> 'a) -> string -> 'b;;


let lit: string -> ('a, 'a) format =
 fun s -> 
  fun k  ->
  k (s)


let int: (int -> 'a, 'a) format =
    fun i ->
