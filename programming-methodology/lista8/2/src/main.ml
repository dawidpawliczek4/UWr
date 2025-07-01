open Ast

let parse (s : string) : expr =
  Parser.prog Lexer.read (Lexing.from_string s)

type value =
  | VInt of int
  | VBool of bool

let eval_op (op : bop) (v1 : value) (v2 : value) : value =
  match op, v1, v2 with
  | Add,  VInt i1, VInt i2 -> VInt (i1 + i2)
  | Sub,  VInt i1, VInt i2 -> VInt (i1 - i2)
  | Mult, VInt i1, VInt i2 -> VInt (i1 * i2)
  | Div,  VInt i1, VInt i2 -> VInt (i1 / i2)
  | Eq,   VInt i1, VInt i2 -> VBool (i1 = i2)
  | Lt,   VInt i1, VInt i2 -> VBool (i1 < i2)
  | Gt,   VInt i1, VInt i2 -> VBool (i1 > i2)
  | Leq,  VInt i1, VInt i2 -> VBool (i1 <= i2)
  | Geq,  VInt i1, VInt i2 -> VBool (i1 >= i2)
  | Neq,  VInt i1, VInt i2 -> VBool (i1 <> i2)
  | _ -> failwith "type error"


(* Evaluation via substitution *)

module Subst = struct

let rec subst (x : ident) (s : expr) (e : expr) : expr =
  match e with
  | Binop (op, e1, e2) -> Binop (op, subst x s e1, subst x s e2)
  | If (p, t, e) -> If (subst x s p, subst x s t, subst x s e)
  | Var y -> if x = y
               then s
               else e
  | Let (y, e1, e2) -> if x = y
                         then Let (y, subst x s e1, e2)
                         else Let (y, subst x s e1, subst x s e2)
  | _ -> e
  
let expr_of_value (v : value) : expr =
  match v with
  | VInt a -> Int a
  | VBool a -> Bool a

let rec eval (e : expr) : value =
  match e with
  | Int n -> VInt n
  | Bool b -> VBool b
  | If (p, t, e) ->
      (match eval p with
      | VBool true -> eval t
      | VBool false -> eval e
      | _ -> failwith "type error")
  | Binop (And, e1, e2) ->
      (match eval e1 with
      | VBool true -> eval e2
      | VBool false -> VBool false
      | _ -> failwith "type error")
  | Binop (Or, e1, e2) ->
      (match eval e1 with
      | VBool false -> eval e2
      | VBool true -> VBool true
      | _ -> failwith "type error")
  | Binop (op, e1, e2) -> eval_op op (eval e1) (eval e2)
  | Let (x, e1, e2) -> let s = expr_of_value (eval e1) in
                       eval (subst x s e2)
  | Var x -> failwith ("unbound value " ^ x)

let interp (s : string) : value =
  eval (parse s)

end


(* Evaluation via environments *)

module Env = struct

module M = Map.Make(String)

type env = value M.t

let rec eval_env (env : env) (e : expr) : value =
  match e with
  | Int n -> VInt n
  | Bool b -> VBool b
  | If (p, t, e) ->
      (match eval_env env p with
      | VBool true -> eval_env env t
      | VBool false -> eval_env env e
      | _ -> failwith "type error")
  | Binop (And, e1, e2) ->
      (match eval_env env e1 with
      | VBool true -> eval_env env e2
      | VBool false -> VBool false
      | _ -> failwith "type error")
  | Binop (Or, e1, e2) ->
      (match eval_env env e1 with
      | VBool false -> eval_env env e2
      | VBool true -> VBool true
      | _ -> failwith "type error")
  | Binop (op, e1, e2) -> eval_op op (eval_env env e1) (eval_env env e2)
  | Let (x, e1, e2) ->
      let r = eval_env env e1 in
      let new_env = M.update x (fun _ -> Some r) env in
      eval_env new_env e2
  | Var x ->
      (match M.find_opt x env with
      | Some v -> v
      | None -> failwith ("unbound value" ^ x))

let eval : expr -> value = eval_env M.empty 

let interp (s : string) : value =
  eval (parse s)

end


(* let alpha_equiv a b : bool =
  let rec alpha_equiv' (a : expr) (b : expr) (env : (ident * ident) list) : bool =
    match a, b with
    | Int a, Int b -> a = b
    | Bool a, Bool b -> a = b
    | If (p1, t1, e1), If (p2, t2, e2) ->
        alpha_equiv' p1 p2 env &&
        alpha_equiv' t1 t2 env &&
        alpha_equiv' e1 e2 env
    | Binop (op1, e11, e12), Binop (op2, e21, e22) ->
        op1 = op2 &&
        alpha_equiv' e11 e21 env &&
        alpha_equiv' e12 e22 env
    | Let (x1, e11, e12), Let (x2, e21, e22) ->
        alpha_equiv' e11 e21 env &&
        alpha_equiv' e12 e22 ((x1, x2) :: env)
    | Var x, Var y -> List.mem (x, y) env
    | _ -> false
  in
  alpha_equiv' a b [] *)

(* rownowazne:
   alpha_equiv (parse "let x = 2 in let y = 5 in x + y") (parse "let y = 2 in let z = 5 in y + z");;
   alpha_equiv (parse "let x = 2 in x + y") (parse "let z = 2 in z + y");;
  
nie:

  alpha_equiv (parse "let x = 2 in x + y") (parse "let y = 2 in y + y");;
*)

type env = (ident * ident) list

(* Check if two expressions are alpha-equivalent *)
let rec alpha_equiv (env : env) (e1 : expr) (e2 : expr) : bool =
  match e1, e2 with
  | Int x, Int y -> x = y
  | Bool x, Bool y -> x = y
  | Var x, Var y ->
    (try List.assoc x env = y with Not_found -> x = y)
  | Binop (op1, ex1, ey1), Binop (op2, ex2, ey2) ->
    op1 = op2 && alpha_equiv env ex1 ex2 && alpha_equiv env ey1 ey2
  | If (c1, t1, f1), If (c2, t2, f2) ->
    alpha_equiv env c1 c2 && alpha_equiv env t1 t2 && alpha_equiv env f1 f2
  | Let (x, ex1, ey1), Let (y, ex2, ey2) ->
    let new_env = (x, y) :: env in
    alpha_equiv env ex1 ex2 && alpha_equiv new_env ey1 ey2
  | _ -> false