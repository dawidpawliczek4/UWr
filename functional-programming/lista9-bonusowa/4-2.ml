module QBF = struct
  type var = string
  type formula = 
    | Var of var               (* zmienne zdaniowe *)
    | Bot                      (* spójnik fałszu (⊥) *)
    | Not of formula           (* negacja (¬φ) *)
    | And of formula * formula (* koniunkcja (φ∧ψ) *)
    | All of var     * formula (* kwantyfikacja uniwersalna (∀p.φ) *)

  type env = var -> bool

  let is_true (f: formula) : bool =
    let rec eval f env =
      match f with
      | Var v -> env v
      | Bot -> false
      | Not f -> not (eval f env)
      | And (f1, f2) -> (eval f1 env) && (eval f2 env)
      | All (v, f) ->
          let env_true x = if x = v then true else env x in
          let env_false x = if x = v then false else env x in
          (eval f env_true) && (eval f env_false)
    in
    eval f (fun _ -> failwith "Unbound variable")
end
