module QBF = struct
  type var = string
  type formula = 
    | Var of var               (* zmienne zdaniowe *)
    | Bot                      (* spójnik fałszu (⊥) *)
    | Not of formula           (* negacja (¬φ) *)
    | And of formula * formula (* koniunkcja (φ∧ψ) *)
    | All of var     * formula (* kwantyfikacja uniwersalna (∀p.φ) *)

  (* Typ środowiska: funkcja mapująca zmienne na wartości bool *)
  type env = var -> bool

  (* Funkcja sprawdzająca wartość formuły w danym środowisku *)
  let is_true (f: formula) : bool =
    let rec eval f env =
      match f with
      | Var v -> env v (* Odczyt zmiennej ze środowiska *)
      | Bot -> false
      | Not f -> not (eval f env)
      | And (f1, f2) -> (eval f1 env) && (eval f2 env)
      | All (v, f) ->
          (* Sprawdzamy dla obu wartości zmiennej (true/false) *)
          let env_true x = if x = v then true else env x in
          let env_false x = if x = v then false else env x in
          (eval f env_true) && (eval f env_false)
    in
    eval f (fun _ -> failwith "Unbound variable") (* Początkowe środowisko *)
end
module NestedQBF = struct
  type 'v inc = Z | S of 'v

  type 'v formula =
    | Var of 'v
    | Bot
    | Not of 'v formula
    | And of 'v formula * 'v formula
    | All of 'v inc formula

  type empty = |

  let absurd (x : empty) = match x with | _ -> .

  let rec eval : type v. v formula -> (v -> bool) -> bool =
    fun f env ->
    match f with
    | Var v -> env v
    | Bot -> false
    | Not f -> not (eval f env)
    | And (f1, f2) -> eval f1 env && eval f2 env
    | All f ->
      let envtrue f = match f with Z -> true | S v -> env v in 
      let envfalse f = match f with Z -> false | S v -> env v in
      (eval f envtrue) && (eval f envfalse)

  let rec is_true (f: empty formula) : bool =
    eval f absurd
end

type 'v env = QBF.var -> 'v

let rec scope_check : type v. v env -> QBF.formula -> v NestedQBF.formula =
  fun env f ->
    match f with
    | QBF.Var x -> NestedQBF.Var (env x) 
    | QBF.Bot -> NestedQBF.Bot          
    | QBF.Not f -> NestedQBF.Not (scope_check env f) 
    | QBF.And (f1, f2) ->               
        NestedQBF.And (scope_check env f1, scope_check env f2)
    | QBF.All (x, f) ->                 
        let env' = fun y ->             
          if y = x then NestedQBF.Z     
          else NestedQBF.S (env y)      
        in
        NestedQBF.All (scope_check env' f)

let f =
  
  QBF.All(QBF.Var "p", QBF.And())