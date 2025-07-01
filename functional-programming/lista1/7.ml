let zero = fun f x -> x

let succ = fun (n: (('a -> 'a) -> 'a -> 'a)) (f: ('a -> 'a)) (x: 'a) -> f (n f x)

let rec cnum_of_int (n: int) = (fun f x -> if n = 0 then x else cnum_of_int (n-1) f (f x) )

let rec int_of_cnum (cnum: ('a -> 'a) -> 'a -> 'a) = cnum (fun x -> x+1) 0

let add x y = cnum_of_int (int_of_cnum x + int_of_cnum y)
let mul x y = cnum_of_int (int_of_cnum x * int_of_cnum y)


let ctrue (x: 'a) (y: 'a) = x
let cfalse (x: 'a) (y: 'a) = y
let is_zero cnum = fun f x -> if cnum f x = x then ctrue else cfalse

let add_2 x y = fun f x0 -> x f (y f x0)
let mult_2 x y = fun f x0 -> x (y f) x0


let fn x = x + 1
