open Ast

type cmd =
  | PushInt of int
  | PushBool of bool
  | Prim of bop
  | CondJmp of cmd list * cmd list
  | Grab           (* wstaw wartosc ze stosu do srodowiska *)
  | Access of int  (* wstaw wartosc ze srodowiska na stos *)
  | EndLet
  | PushClo of cmd list
  | Call
  | Return
  | Raise
  | BeginTry of cmd list * cmd list
  | EndTry
            
type vm_value =
  | VMInt of int
  | VMBool of bool
  | VMClosure of cmd list * vm_value list
  | VMRetAddr of cmd list * vm_value list

let eval_vm_op (op : bop) (v1 : vm_value) (v2 : vm_value) : vm_value =
  match op, v1, v2 with
  | Add,  VMInt i1, VMInt i2 -> VMInt (i1 + i2)
  | Sub,  VMInt i1, VMInt i2 -> VMInt (i1 - i2)
  | Mult, VMInt i1, VMInt i2 -> VMInt (i1 * i2)
  | Div,  VMInt i1, VMInt i2 -> VMInt (i1 / i2)
  | Eq,   VMInt i1, VMInt i2 -> VMBool (i1 = i2)
  | Lt,   VMInt i1, VMInt i2 -> VMBool (i1 < i2)
  | Gt,   VMInt i1, VMInt i2 -> VMBool (i1 > i2)
  | Leq,  VMInt i1, VMInt i2 -> VMBool (i1 <= i2)
  | Geq,  VMInt i1, VMInt i2 -> VMBool (i1 >= i2)
  | Neq,  VMInt i1, VMInt i2 -> VMBool (i1 <> i2)
  | _ -> failwith "type error"

let stack_size = 4096

let print_value v =
  print_endline
    (match v with
    | VMInt  n     -> string_of_int n
    | VMBool true  -> "true"
    | VMBool false -> "false"
    | VMClosure _  -> "<fun>"
    | VMRetAddr _  -> "<ret-addr>")

let print_cmdlist cmd_list = 
  let string_of_bop bop =
    match bop with
    | Add -> "Add"
    | Sub -> "Sub"
    | Mult -> "Mult"
    | Div -> "Div"
    | Eq -> "Eq"
    | Lt -> "Lt"
    | Gt -> "Gt"
    | Leq -> "Leq"
    | Geq -> "Geq"
    | Neq -> "Neq"
    | And -> "And"
    | Or -> "Or"
  in
  List.iter (fun cmd -> 
    match cmd with
    | PushInt n -> print_endline ("PushInt " ^ string_of_int n)
    | PushBool b -> print_endline ("PushBool " ^ string_of_bool b)
    | Prim op -> print_endline ("Prim " ^  string_of_bop op)
    | CondJmp (t, e) -> print_endline "CondJmp"
    | Grab -> print_endline "Grab"
    | Access n -> print_endline ("Access " ^ string_of_int n)
    | EndLet -> print_endline "EndLet"
    | PushClo q -> print_endline "PushClo"
    | Call -> print_endline "Call"
    | Return -> print_endline "Return"
    | Raise -> print_endline "Raise"
    | BeginTry (p1, q) -> print_endline "BeginTry"
    | EndTry -> print_endline "EndTry"
  ) cmd_list

let exec_prog p =
  (* Create empty stack *)
  let stack = Array.make stack_size (VMInt 0) in
  (* Stack pointer *)
  let sp = ref stack_size in
  (* NOWE - exception handler stack *)
  let exn_stack = Stack.create () in
  (* Push a value on a stack *)
  let push v = sp := !sp - 1; stack.(!sp) <- v in
  (* Pop a value from a stack *)
  let pop () = let v = stack.(!sp) in sp := !sp + 1; v in
  let rec exec (p : cmd list) (env : vm_value list) : vm_value =
    match p with
    | [] -> pop ()
    | PushInt n :: p' -> push (VMInt n); exec p' env
    | PushBool b :: p' -> push (VMBool b); exec p' env
    | Prim op :: p' ->
      let v1 = pop () in
      let v2 = pop () in
      push (eval_vm_op op v2 v1);
      exec p' env
    | CondJmp (t, e) :: p' ->
      (match pop () with
      | VMBool true  -> exec (t @ p') env
      | VMBool false -> exec (e @ p') env
      | _ -> failwith "error")
    | Grab :: p' -> exec p' (pop () :: env)
    | Access n :: p' -> push (List.nth env n); exec p' env
    | EndLet :: p' -> exec p' (List.tl env)
    | PushClo q :: p' -> push (VMClosure (q, env)); exec p' env
    | Call :: p' ->
      (match pop () with
      | VMClosure (q, env') ->
        let v = pop () in
        push (VMRetAddr (p', env));
        exec q (v :: env')
      | _ -> failwith "error")
    | Return :: _ ->
      let v = pop () in
      (match pop () with
      | VMRetAddr (p, env') -> push v; exec p env'
      | _ -> failwith "error")
    (* | BeginTry(p1, q) :: p' ->
      Stack.push (q, p', env) exn_stack;
      exec p1 env
    | EndTry :: p' ->
      if Stack.is_empty exn_stack then failwith "error"
      else let (handler_p, rest_of_program, handler_env) = Stack.pop exn_stack in
      exec rest_of_program handler_env
    | Raise :: _ ->
      if Stack.is_empty exn_stack then failwith "unhandled exception"
      else let (handler_p, rest_of_program, handler_env) = Stack.pop exn_stack in
      let _ = exec handler_p handler_env in exec rest_of_program env *)
    | BeginTry (p1, q) :: p' ->
      Stack.push (q, p', env) exn_stack;
 
      exec p1 env
 
    | EndTry :: p' ->
      if not (Stack.is_empty exn_stack) then ignore (Stack.pop exn_stack);
      exec p' env
    | Raise :: _ ->
      if Stack.is_empty exn_stack then failwith "unhandled exception"
      else let (handler_p, rest_of_program, handler_env) = Stack.pop exn_stack in
      print_cmdlist handler_p;
      print_cmdlist rest_of_program;
      ignore(exec handler_p handler_env); exec rest_of_program (handler_env @ env)
      (* ignore(exec handler_p handler_env); exec rest_of_program env *)
  in
  exec p []
