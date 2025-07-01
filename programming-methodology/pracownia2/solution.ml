(* abstract syntax tree *)

type bop = Mult | Div | Add | Sub | Eq | Lt | Gt | Leq | Geq | Neq

type ident = string

type expr =
  | Int of int
  | Bool of bool
  | Binop of bop * expr * expr
  | If of expr * expr * expr
  | Var of ident
  | Let of ident * expr * expr

let alphaeq (e1 : expr) (e2 : expr) : bool =
  let rec alpha_equiv (env : (ident * ident) list) (e1 : expr) (e2 : expr) =
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
  in alpha_equiv [] e1 e2

let free_vars e =
  let rec free_vars' e =
    match e with
    | Int _ -> []
    | Bool _ -> []
    | Var x -> [x]
    | Binop (_, e1, e2) -> free_vars' e1 @ free_vars' e2
    | If (e1, e2, e3) -> free_vars' e1 @ free_vars' e2 @ free_vars' e3
    | Let (x, e1, e2) -> List.filter (fun y -> y <> x) (free_vars' e1 @ free_vars' e2)
  in List.sort_uniq compare (free_vars' e)

let are_equivalent e e1 e2 =
  alphaeq e1 e2 && List.for_all (fun x -> List.mem x (free_vars e)) (free_vars e1 @ free_vars e2)

let rec subst (e: expr) (e1: expr) (e2: expr) =
  if e = e1 then e2 else
  match e with
  | Let (x, e1', e2') -> Let (x, subst e1' e1 e2, subst e2' e1 e2)
  | Binop (op, e1', e2') -> Binop (op, subst e1' e1 e2, subst e2' e1 e2)
  | If (e1', e2', e3') -> If (subst e1' e1 e2, subst e2' e1 e2, subst e3' e1 e2)
  | _ -> e

let extract_all_subexpressions e =  
  let rec aux e =
    match e with
    | Binop (_, e1, e2) -> e :: (aux e1 @ aux e2)
    | If (e1, e2, e3) -> e :: (aux e1 @ aux e2 @ aux e3)
    | Let (_, e1, e2) -> e :: (aux e1 @ aux e2)
    | _ -> []
  in 
  match e with
  | Binop (_, e1, e2) -> (aux e1 @ aux e2)
  | If (e1, e2, e3) -> (aux e1 @ aux e2 @ aux e3)
  | Let (_, e1, e2) -> (aux e1 @ aux e2)
  | _ -> []

let find_equiv_subexpr (e: expr) : expr list =
  let subexprs = extract_all_subexpressions e in
  let rec find_equiv_subexpr' ex subexprs acc =
    match subexprs with
    | [] -> acc
    | hd :: tl -> 
      if are_equivalent e hd ex then find_equiv_subexpr' ex tl (hd :: acc)
      else find_equiv_subexpr' ex tl acc
  in 
  let rec find_not_empty_equiv_subexprs subexprs =
    match subexprs with
    | [] -> []
    | hd :: tl -> 
      let equiv_subexprs = find_equiv_subexpr' hd tl [] in
      if equiv_subexprs <> [] then equiv_subexprs
      else find_not_empty_equiv_subexprs tl
  in find_not_empty_equiv_subexprs subexprs

let cse (e: expr) : expr option =
    let equiv_subexprs = find_equiv_subexpr e in   
    if equiv_subexprs = [] then None
    else
    Some (Let ("v0", List.hd equiv_subexprs, subst e (List.hd equiv_subexprs) (Var "v0")))

(* 
"x + let x = 3 in x * 10 + x * 10"   
parsed:
Binop(Add, Var "x", Let("x", Int 3, Binop(Add, Binop(Mult, Var "x", Int 10), Binop(Mult, Var "x", Int 10))))
*)