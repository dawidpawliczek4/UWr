
module QBF = struct
  type var = string
  type formula = 
    | Var of var               (* zmienne zdaniowe *)
    | Bot                      (* spójnik fałszu (⊥) *)
    | Not of formula           (* negacja (¬φ) *)
    | And of formula * formula (* koniunkcja (φ∧ψ) *)
    | All of var     * formula (* kwantyfikacja uniwersalna (∀p.φ) *)
  module StringMap = Map.Make(String)

  let is_true (f: formula) : bool =       
     let env = StringMap.empty in
    let rec aux f env =
    match f with
    | Var v -> begin match StringMap.find_opt v env with 
      | Some v -> v
      | None -> failwith "zmienna wolna!" 
        end
    | Bot -> false
    | Not f -> not (aux f env)
    | And (f1,f2) -> (aux f1 env) && (aux f2 env)
    | All (v, f) -> let env1 = StringMap.add v true env in 
        let env2 = StringMap.add v false env in
        (aux f env1) && (aux f env2)
    in aux f env

end


