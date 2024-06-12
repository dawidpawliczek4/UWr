open Ast

module H = Map.Make(String)

type env = int ref H.t

let lookup_var env x =
  match H.find_opt x env with
  | Some l -> !l
  | None   -> failwith ("Unbound variable " ^ x)

let assign_var env x v =
  match H.find_opt x env with
  | Some l -> l := v
  | None   -> failwith ("Unbound variable " ^ x)

let declare_var env x =
  H.add x (ref 0) env

let eval_binop op =
  match op with
  | Mul -> ( * )
  | Div -> ( / )
  | Add -> ( + )
  | Sub -> ( - )

let rec eval_aexp env e =
  match e with
  | Int n -> n
  | Var x -> lookup_var env x
  | Binop(op, e1, e2) ->
    eval_binop op (eval_aexp env e1) (eval_aexp env e2)    

let eval_cmpop op =
  match op with
  | Eq  -> ( = )
  | Neq -> ( <> )
  | Lt  -> ( < )
  | Gt  -> ( > )
  | Leq -> ( <= )
  | Geq -> ( >= )

let rec eval_bexp env e =
  match e with
  | Bool b -> b
  | Cmp(op, e1, e2) ->
    eval_cmpop op (eval_aexp env e1) (eval_aexp env e2)
  | And(e1, e2) ->
    eval_bexp env e1 && eval_bexp env e2
  | Or(e1, e2) ->
    eval_bexp env e1 || eval_bexp env e2
  | Not e -> not (eval_bexp env e)
  
(*  *)
type result =
| Normal of unit
| Excep

let rec eval_stmt env s : result =
  match s with
  | Block ss    ->  List.iter (fun s -> match eval_stmt env s with | Excep -> raise (Failure "") | Normal _ -> ()) ss; Normal ()
  | Assgn(x, e) -> assign_var env x (eval_aexp env e); Normal ()
  | If(e, s1, s2) ->
    if eval_bexp env e then eval_stmt env s1
    else eval_stmt env s2
  | While(e, s) ->
    while eval_bexp env e do
      match eval_stmt env s with
      | Excep -> raise (Failure "")
      | Normal _ -> ()
    done; Normal ()
  | Read x ->
    begin
      try
    read_line () |> int_of_string |> assign_var env x; Normal()
      with Failure _ -> Excep
    end
  | Write e ->
    eval_aexp env e |> string_of_int |> print_endline; Normal ()
  | Try(s1, s2) ->
     begin
      try      
    match eval_stmt env s1 with
      | Normal _ as result -> result
      | Excep -> eval_stmt env s2       
     with
       | Failure _ -> eval_stmt env s2
    end
  | Raise -> Excep

let run_prog (xs, stmt) =
  let env = List.fold_left declare_var H.empty xs in
  eval_stmt env stmt
