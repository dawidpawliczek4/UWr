(* zad 1 *)
exception Found

let exists f xs =
  let check_and_raise _ x =
    if f x then raise Found
  in
  try
    List.fold_left check_and_raise () xs;  (* Use fold_left to traverse the list *)
    false  (* If no exception was raised, return false *)
  with
    Found -> true  (* If the exception was raised, return true *)


(* zad 2 *)

let find (type t) f (xs : t list) =
  let exception Found of t in
  let check_and_raise _ x =
    if f x then raise (Found x)
  in
  try
    List.fold_left check_and_raise () xs;
    raise Not_found
  with
    Found x -> x


let is_even x = x mod 2 = 0
let list1 = [1; 3; 5; 6; 7]
let list2 = [1; 3; 7]