(* 
  type rpn_cmd = 
  | Push of int 
  | RAdd
  | RMult

  type rpn = rpn_cmd list   

  type expr =
  | Int of int
  | Add of expr * expr 
  | Mult of expr * expr
*)

(* udowodnic ze 

  eval_rpn (to_rpn e) [] = eval e

  udowodnimy pomocnicze
  eval_rpn (to_rpn e) s = eval e :: s

  1. podstawa indukcji
  to_rpn (int n) = [push n]
  eval_rpn([push n]) s = n :: s
  eval(int n) :: s = n :: s

  2. krok indukcyjny
  zalozmy ze tw, jest prawdziwe dla e1 e2

  a) add

  to_rpn (add(e1,e2) = to_rpn e1 @ to_rpn e2 @ [radd]
  eval_rpn(to_rpn e1 @ to_rpn e2 @ [radd]) s = eval_rpn([radd]) (eval e2 :: eval e1 :: s) = (eval e1 + eval e2) :: s
  zgodne z
  eval(add(e1,e2)) :: s = (eval e1 + eval e2) :: s

  b) mult
  ...
  eval_rpn (to_rpn Mult(e1,e2)) s = eval e1 * eval e2 :: s

  3. koniec
  eval_rpn (to_rpn e) [] = eval e :: [] = [eval e]
  eval_rpn zwraca liczbe gdy stos wejsciowuy jest pusty i pozostaje tylko jeden element na stosie, otrzymujemy
  eval_rpn (to_rpn e) [] = eval e
  co konczy dowod

*)