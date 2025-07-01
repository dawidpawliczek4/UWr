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
  (*  *)
  | VPair(v1, v2), PPair(p1, p2) -> 
    (match p1, p2 with
    | PVar id1, PVar id2 when id1 = id2 ->
      failwith "error - multiple bindings of the same variable"
    | _, _ -> 
      (match match_pattern env v1 p1 with
      | None -> None
      | Some env -> match_pattern env v2 p2))
  | _, PPair _ -> None
§