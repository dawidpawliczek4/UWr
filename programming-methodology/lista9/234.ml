type expr =
| Int of int
| Add of expr * expr 
| Mult of expr * expr


let rec eval (e : expr) : int =
match e with
| Int n -> n
| Add (e1, e2) -> eval e1 + eval e2 | Mult (e1, e2) -> eval e1 * eval e2


type rpn_cmd = 
  | Push of int 
  | RAdd
  | RMult

type rpn = rpn_cmd list

let rec to_rpn (e : expr) : rpn =
match e with
| Int n -> [Push n]
| Add (e1, e2) -> to_rpn e1 @ to_rpn e2 @ [RAdd]
| Mult (e1, e2) -> to_rpn e1 @ to_rpn e2 @ [RMult]
let rec eval_rpn (r : rpn) (s : int list) : int = match r, s with
| [], [n] -> n
| Push n :: r', _ -> eval_rpn r' (n :: s)
| RAdd :: r', n1 :: n2 :: s' -> eval_rpn r' (n2 + n1 :: s') | RMult :: r', n1 :: n2 :: s' -> eval_rpn r' (n2 * n1 :: s') | _,_ -> failwith "error!"

(* zad 2 *)
let rec from_rpn (r : rpn) : expr =
 let rec aux r stack = 
  match r with 
  | [] -> (
    match stack with
    | [e] -> e  (* Ostatecznie na stosie powinno zostać tylko jedno wyrażenie, które jest wynikiem *)
    | _ -> failwith "Invalid RPN expression or stack state"
  )
| Push n :: t -> aux t (Int n :: stack)  (* Dodajemy liczbę jako wyrażenie do stosu *)
| RAdd :: t -> (
    match stack with
    | e1 :: e2 :: s -> aux t (Add (e2, e1) :: s)  (* Zdejmujemy dwa wyrażenia ze stosu, dodajemy je i odkładamy wynik z powrotem na stos *)
    | _ -> failwith "Not enough elements for addition"
  )
| RMult :: t -> (
    match stack with
    | e1 :: e2 :: s -> aux t (Mult (e2, e1) :: s)  (* Podobnie jak w dodawaniu, ale mnożymy *)
    | _ -> failwith "Not enough elements for multiplication"
  )
in aux r []

let rpn_example1 = [Push 3; Push 4; RAdd];; 
let rpn_example2 = [Push 5; Push 6; RMult];;
let rpn_example3 = [Push 2; Push 3; RAdd; Push 4; RMult];;
let rpn_example4 = [Push 10; RAdd];;
(*  *)

(* zad 3 *)

let rec random_expr max_depth =
  if max_depth = 0 then
    Int (Random.int 20)
  else
    match Random.int 3 with
    | 0 -> Int (Random.int 20)
    | 1 -> Add (random_expr (max_depth - 1), random_expr (max_depth - 1))
    | 2 -> Mult (random_expr (max_depth - 1), random_expr (max_depth - 1))
    | _ -> failwith "unexpected case"

let test max_depth n =
  let rec helper count =
    if count = 0 then true
    else
      let expr = random_expr max_depth in
      let rpn = to_rpn expr in
      let expr_from_rpn = from_rpn rpn in
      if expr = expr_from_rpn then
        helper (count - 1)
      else
        false
  in helper n

let test_ce max_depth n =
  let rec helper count =
    if count = 0 then None
    else
      let expr = random_expr max_depth in
      let rpn = to_rpn expr in
      let expr_from_rpn = from_rpn rpn in
      if expr = expr_from_rpn then
        helper (count - 1)
      else
        Some expr  (* Zwraca wyrażenie, które nie spełnia warunku *)
  in helper n
