
(* strumien - jakas funkcja z int w t , s 0 - pierwszy element, s 1 drugi, etc *)

let hd (str: int -> 'a) = str 0
let tail (str: int -> 'a) = fun x -> str (x + 1)

let add (str: int -> 'a) i = fun x -> (str x) + i

let map (f: 'a -> 'b) (str: int -> 'a) = fun x -> f (str x)

let map2 (f) (str1: int -> 'a) (str2: int -> 'b) = fun x -> f (str1 x) (str2 x)

let replace str i v = fun x -> if x = i then v else str x

let take_every n str = fun x -> str (x * n)

let strumien x = -x
(* zad 4 -- ?? *)

let scan f a s =
  let rec scan' i =
    if i = 0 then f a (s 0)
    else f (scan' (i - 1)) (s i)
  in scan'

(* zad 5 -- ?? *)

let rec tabulate ?(fi=0) li str =
  if li <= fi then [(str li)] else ( (str li) :: tabulate ~fi:fi (li-1) str)
