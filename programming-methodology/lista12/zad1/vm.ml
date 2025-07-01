let hstack = ref []

let rec exec (p : cmd list) (s : vm_value list) (env : vm_value list) : vm_value =
  match p, s with
  | [], [v] -> v
  | PushInt n :: p', _ -> exec p' (VMInt n :: s) env
  | PushBool b :: p', _ -> exec p' (VMBool b :: s) env
  | Prim op :: p', (v1 :: v2 :: s) -> exec p' (eval_vm_op op v2 v1 :: s) env
  | CondJmp (t, e) :: p', VMBool v :: s' -> if v then exec (t @ p') s' env
                                            else exec (e @ p') s' env
  | Grab :: p', v :: s' -> exec p' s' (v :: env)
  | Access n :: p', _ -> exec p' (List.nth env n :: s) env
  | EndLet :: p', _ -> exec p' s (List.tl env)
  | PushClo q :: p', _ -> exec p' (VMClosure (q, env) :: s) env
  | Call :: p', VMClosure (q, env') :: v :: s' ->
     exec q (VMRetAddr (p', env) :: s') (v :: env')
  | Return :: _, v :: VMRetAddr (p, env') :: s' -> exec p (v :: s') env'
  (*  *)
  | BeginTry(p1, q) :: p', _ ->
    hstack := (q @ p', s, env) :: !hstack;
    exec (p1 @ p') s env
  | EndTry :: p', _ ->
    hstack := List.tl !hstack;
    exec p' s env
  | Raise :: _, _ ->
    (match !hstack with
    | [] -> failwith "unhandled exception"
    | (q, s', env') :: hst ->
      hstack := hst;
      exec q s' env')
  | _, _ -> failwith "error"
       
let exec_prog p = exec p [] []