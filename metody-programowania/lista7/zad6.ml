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