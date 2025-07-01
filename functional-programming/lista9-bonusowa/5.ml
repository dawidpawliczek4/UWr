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
