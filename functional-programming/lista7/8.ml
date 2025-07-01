type symbol = string

type 'v term =
  | Var of 'v
  | Sym of symbol * 'v term list

let return x = Var x

let rec bind t f =
  match t with
  | Var v -> f v
  | Sym (sym, terms) -> Sym (sym, List.map (fun t -> bind t f) terms)

(* 
let example_function x = Sym ("f", [Var x; Var (x + 1)])

let term1 = return 42
let term2 = bind term1 example_function *)
