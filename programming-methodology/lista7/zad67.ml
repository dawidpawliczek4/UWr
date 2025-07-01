type ident = string

type qbf =
  | Top
  | Bot
  | Var of ident
  | Forall of ident * qbf
  | Exists of ident * qbf
  | Not of qbf
  | Conj of qbf * qbf
  | Disj of qbf * qbf

let subst (x : ident) (s : qbf) (f : qbf) : qbf =
  let rec subst' f =
    match f with
    | Top -> Top
    | Bot -> Bot
    | Var y -> if x = y then s else Var y
    | Forall (y, f) -> if x = y then Forall (y, f) else Forall (y, subst' f)
    | Exists (y, f) -> if x = y then Exists (y, f) else Exists (y, subst' f)
    | Not f -> Not (subst' f)
    | Conj (f1, f2) -> Conj (subst' f1, subst' f2)
    | Disj (f1, f2) -> Disj (subst' f1, subst' f2)
  in
  subst' f

  
module M = Map.Make(String)
type env = bool M.t

let eval (f : qbf) : bool =  
  let rec eval' f =
    match f with
    | Top -> true
    | Bot -> false
    | Var _ -> failwith "free variable"
    | Forall (x, fi) -> 
      let a = eval' (subst x Top fi) in
      let b = eval' (subst x Bot fi) in
      a && b
    | Exists (x, fi) ->
      let a = eval' (subst x Top fi) in
      let b = eval' (subst x Bot fi) in
      a || b
    | Not f -> not (eval' f)
    | Conj (f1, f2) -> eval' f1 && eval' f2
    | Disj (f1, f2) -> eval' f1 || eval' f2        
    in
    eval' f

let eval_env (env : env) (f : qbf) : bool = 
  let rec eval' env f =
    match f with
    | Top -> true
    | Bot -> false
    | Var x -> M.find x env
    | Forall (x, f) -> 
      let env' = M.add x true env in
      let env'' = M.add x false env
      in eval' env' f && eval' env'' f
    | Exists (x, f) ->
      let env' = M.add x false env in
      let env'' = M.add x true env
      in eval' env' f || eval' env'' f
    | Not f -> not (eval' env f)
    | Conj (f1, f2) -> eval' env f1 && eval' env f2
    | Disj (f1, f2) -> eval' env f1 || eval' env f2
  in
  eval' env f