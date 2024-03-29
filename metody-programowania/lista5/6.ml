type 'v formula =
  | Var of 'v
  | Neg of 'v formula
  | Conj of 'v formula * 'v formula
  | Disj of 'v formula * 'v formula
  
type 'v nnf =
| NNFLit of bool * 'v
| NNFConj of 'v nnf * 'v nnf 
| NNFDisj of 'v nnf * 'v nnf

let rec to_nnf = function
  | Var v -> Var v
  | Neg (Var v) -> Neg (Var v)
  | Neg (Neg f) -> to_nnf f
  | Neg (Conj (f1, f2)) -> Disj (to_nnf (Neg f1), to_nnf (Neg f2))
  | Neg (Disj (f1, f2)) -> Conj (to_nnf (Neg f1), to_nnf (Neg f2))
  | Conj (f1, f2) -> Conj (to_nnf f1, to_nnf f2)
  | Disj (f1, f2) -> Disj (to_nnf f1, to_nnf f2)


  (* zad 7 *)

let rec eval_formula sigma = function
  | Var v -> sigma v
  | Neg f -> not (eval_formula sigma f)
  | Conj (f1, f2) -> eval_formula sigma f1 && eval_formula sigma f2
  | Disj (f1, f2) -> eval_formula sigma f1 || eval_formula sigma f2

(* 
eval_nnf σ (to_nnf φ) = eval_formula σ φ

1. Baza indukcji
  eval_nnf σ (to_nnf (Var v)) = eval_formula σ (Var v)
  eval_nnf σ (Var v) = eval_formula σ (Var v)
  σ v = σ v

2. Krok indukcyjny
  wezmy dowolna f i zalozmy
    eval_nnf σ (to_nnf f) = eval_formula σ f  
    Pokażemy, że dla każdej formuły f spełnione jest:

    f = Neg (f)
    eval_nnf σ (to_nnf (Neg (f))) = eval_formula σ (Neg (f))
    eval_nnf σ (Neg (f)) = eval_formula σ (Neg (f))
    not (eval_nnf σ (to_nnf (f))) = not (eval_formula σ (f))
    not (σ f) = not (σ f)

    f = Conj (f1, f2)
    eval_nnf σ (to_nnf (Conj (f1, f2))) = eval_formula σ (Conj (f1, f2))
    eval_nnf σ (Conj (to_nnf f1, to_nnf f2)) = eval_formula σ (Conj (f1, f2))
    eval_nnf σ (to_nnf f1) && eval_nnf σ (to_nnf f2) = eval_formula σ f1 && eval
    eval_formula σ f1 && eval_formula σ f2 = eval_formula σ f1 && eval_formula σ f2

    f = Disj (f1, f2)
    eval_nnf σ (to_nnf (Disj (f1, f2))) = eval_formula σ (Disj (f1, f2))
    eval_nnf σ (Disj (to_nnf f1, to_nnf f2)) = eval_formula σ (Disj (f1, f2))
    eval_nnf σ (to_nnf f1) || eval_nnf σ (to_nnf f2) = eval_formula σ f1 || eval
    eval_formula σ f1 || eval_formula σ f2 = eval_formula σ f1 || eval_formula σ f2

    Wszystkie przypadki spełniają założenie indukcyjne, więc teza jest prawdziwa.

*)