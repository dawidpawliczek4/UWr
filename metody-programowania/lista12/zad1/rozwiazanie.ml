let rec exec (p : cmd list) (s : vm_value list) (env : vm_value list) (withh : (cmd list * vm_value list * vm_value list) list): vm_value =
  match p, s with
  | [], [v] -> v
  | PushInt n :: p', _ -> exec p' (VMInt n :: s) env withh
  | PushBool b :: p', _ -> exec p' (VMBool b :: s) env withh
  | Prim op :: p', (v1 :: v2 :: s) -> exec p' (eval_vm_op op v2 v1 :: s) env withh
  | CondJmp (t, e) :: p', VMBool v :: s' -> if v then exec (t @ p') s' env withh
                                            else exec (e @ p') s' env withh
  | Grab :: p', v :: s' -> exec p' s' (v :: env) withh
  | Access n :: p', _ -> exec p' (List.nth env n :: s) env withh
  | EndLet :: p', _ -> exec p' s (List.tl env) withh
  | PushClo q :: p', _ -> exec p' (VMClosure (q, env) :: s) env withh
  | Call :: p', VMClosure (q, env') :: v :: s' ->
     exec q (VMRetAddr (p', env) :: s') (v :: env') withh
  | Return :: _, v :: VMRetAddr (p, env') :: s' -> exec p (v :: s') env' withh
  (*  *)
  | BeginTry(p1, q) :: p', _ ->
    exec (p1 @ p') s env ((q,s,env) :: withh)
  | EndTry :: p', _ ->
    exec p' s env (List.tl withh)
  | Raise :: _, _ ->
    (match withh with
    | [] -> failwith "unhandled exception"
    | (q, s', env') :: withh' ->
      exec q s' env' withh') 
  | _, _ -> failwith "error"
       
let exec_prog p = exec p [] [] [] 