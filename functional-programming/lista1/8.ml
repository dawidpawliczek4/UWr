type cbool = { cbool : 'a. 'a -> 'a -> 'a }
type cnum = { cnum : 'a. ('a -> 'a) -> 'a -> 'a }

let even n = {
  cbool = fun tt ff -> fst (n.cnum (fun (a, b) -> (b, a)) (tt, ff))
}

(* cbool *)
let cbool_of_bool b =
  if b then
   {cbool = fun x y -> x}
  else
    {cbool = fun x y -> y}

let bool_of_cbool f = f.cbool true false

let cand x y = x.cbool true false && y.cbool true false
let cand_2 x y = {
  cbool =
  fun ct cf -> x.cbool (y.cbool ct cf) cf
}

let cor x y = x.cbool true false || y.cbool true false
let cor_2 x y = {
  cbool =
  fun ct cf -> x.cbool ct (y.cbool ct cf)
}

(* cnum *)

let zero = {
  cnum = fun f x -> x
}

let succ n = {
  cnum =
    fun f x -> f (n.cnum f x)
}

let rec cnum_of_int (n: int) =
    if n = 0 then { cnum = fun f x -> x }
    else{
      cnum = fun f x -> f ((cnum_of_int (n-1)).cnum f x)
}

let rec int_of_cnum cnum = cnum.cnum (fun x -> x+1) 0

let add x y = cnum_of_int (int_of_cnum x + int_of_cnum y)
let mul x y = cnum_of_int (int_of_cnum x * int_of_cnum y)


let ctrue = { cbool = fun x y -> x}
let cfalse = { cbool = fun x y -> y}
let is_zero cnum = fun f x -> if cnum.cnum f x = x then ctrue else cfalse

let add_2 x y = { cnum = fun f x0 -> x.cnum f (y.cnum f x0)}
let mult_2 x y = { cnum = fun f x0 -> x.cnum (y.cnum f) x0}
