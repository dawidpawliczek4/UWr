let _ = fun x -> x

let ident (x: int) : int = x
let ident x = x + 0

let compose f g x = f (g x)

let first x y = x

let f (a: 'a) (b: 'a) : 'a = a

(* 2 *)
let f a = failwith "test"


let rec f x = f x
