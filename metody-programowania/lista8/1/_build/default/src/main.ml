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


let cp_binop_int_int op e1 e2 =
  match op with
  | Add -> Int (e1 + e2)
  | Sub -> Int (e1 - e2)
  | Mult -> Int (e1 * e2)
  | Div -> Int (e1 / e2)
  | Eq -> Bool (e1 = e2)
  | Lt -> Bool (e1 < e2)
  | Gt -> Bool (e1 > e2)
  | Leq -> Bool (e1 <= e2)
  | Geq -> Bool (e1 >= e2)
  | Neq -> Bool (e1 <> e2)
  | _ -> failwith "type error"

let cp_binop_bool_bool op e1 e2 =
  match op with
  | And -> Bool (e1 && e2)
  | Or -> Bool (e1 || e2)
  | Eq -> Bool (e1 = e2)
  | _ -> failwith "type error"

let cp_binop op e1 e2 =
  match e1, e2 with
  | Int n1, Int n2 -> cp_binop_int_int op n1 n2
  | Bool b1, Bool b2 -> cp_binop_bool_bool op b1 b2
  | _ -> Binop (op, e1, e2)

let rec cp e = match e with
  | Int n -> Int n
  | Bool b -> Bool b
  | Binop (op, e1, e2) -> 
    let e1' = cp e1 in
    let e2' = cp e2 in
    cp_binop op e1' e2'   
  | If (p, t, e) ->     
    begin
      match cp p with 
      | Bool true -> cp t
      | Bool false -> cp e
      | _ -> If (cp p, cp t, cp e)
    end
  | Let (x, e1, e2) -> 
      let e1' = cp e1 in
      begin
      match e1' with
      | Int _ -> cp (Subst.subst x e1' e2)
      | Bool _ -> cp (Subst.subst x e1' e2)
      | _ -> Let (x, e1', cp (Subst.subst x (Var x) e2))
      end
  | Var x -> Var x