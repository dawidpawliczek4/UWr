(* ZADANIE 1 *)
(* zmodyfikuj vm.ml parser i lexer *)

(* ZADANIE 4 *)
(* dla let musimy zmienić w ast ident na patter*)
(* zmodyfikuj let dla eval_env w eval.ml *)
(* zmodyfikuj parser *)
(* rozwiaz konflikt w stdlib *)
(*------------------------------------------------*)
(* dla fun zmien ident na pattern w ast *)
(* w eval.ml zmien Fun i App w eval_env *)
(* w eval zmien ident w VClosure na pattern *)
(* w parserze dodaj patterns analogicznie do idents i zmodyfikuj reszte *)

(* ZADANIE 5 *)
let rec match_pattern env v p =
  match v, p with
  | _,       PWildcard  -> Some env
  | VUnit,   PUnit      -> Some env
  | _,       PUnit      -> None
  | VInt n,  PInt m when n = m -> Some env
  | _,       PInt _     -> None
  | VBool x, PBool y when x = y -> Some env
  | _,       PBool _    -> None
  | _,       PVar  x    -> Some (M.add x v env)
  | VCtor(c1, v), PCtor(c2, p) when c1 = c2 ->
    match_pattern env v p
  | _, PCtor _ -> None
  | VPair(v1, v2), PPair(p1, p2) ->
    match p1, p2 with
    | PVar id1, PVar id2 when id1 = id2 ->
      failwith "error - multiple bindings of the same variable"
    | _, _ -> 
      (match match_pattern env v1 p1 with
      | None -> None
      | Some env -> match_pattern env v2 p2)
  | _, PPair _ -> None

(* ZADANIE 6 *)
(* AST *)
and clause = 
  | Normal of pattern * expr
  | As of pattern * ident * expr

(* EVAL *)
and match_clauses env v cs =
  match cs with
  | [] -> failwith "match failure"
  | Normal (p, e) :: cs ->
    (match match_pattern env v p with
    | Some env -> eval_env env e
    | None -> match_clauses env v cs)
  | As (p,id,e) :: cs -> 
    let new_env = (M.add id v env) in
    (match match_pattern new_env v p with
    | Some env -> eval_env env e
    | None -> match_clauses new_env v cs)

(* zmien lexer i parser *)

