
(* a -> a -> a *)

let ctrue (x: 'a) (y: 'a) = x
let cfalse (x: 'a) (y: 'a) = y

let cbool_of_bool b =
  if b then
    fun (x: 'a) (y: 'a) -> x
  else
    fun (x: 'a) (y: 'a) -> y

let bool_of_cbool f = f true false

let cand x y = x true false && y true false
let cand_2 x y = fun ct cf -> x (y ct cf) cf

let cor x y = x true false || y true false
let cor_2 x y = fun ct cf -> x ct (y ct cf)
