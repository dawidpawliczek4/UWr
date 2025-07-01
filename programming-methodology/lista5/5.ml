type 'v nnf =
  | NNFLit of bool * 'v
  | NNFConj of 'v nnf * 'v nnf 
  | NNFDisj of 'v nnf * 'v nnf

let rec neg_nnf = function
| NNFLit (b, v) -> NNFLit (not b, v)
| NNFConj (f1, f2) -> NNFDisj (neg_nnf f1, neg_nnf f2)
| NNFDisj (f1, f2) -> NNFConj (neg_nnf f1, neg_nnf f2)

let rec eval_nnf eval nnf  = 
  match nnf with
  | NNFLit (b, v) -> if b then not (eval v) else eval v
  | NNFConj (nnf1, nnf2) -> (eval_nnf eval nnf1) && (eval_nnf eval nnf1)
  | NNFDisj (nnf1, nnf2) -> (eval_nnf eval nnf1) || (eval_nnf eval nnf2)

(* 
  pokazemy, ze
  eval_nnf sigma (neg_nnf f) == not (eval_nnf sigma f)
  przez indukcje po f
  1. Baza indukcji
  f = NNFLit (b, v)
  eval_nnf sigma (neg_nnf (NNFLit (b, v))) == not (eval_nnf sigma (NNFLit (b, v)))
  eval_nnf sigma (NNFLit (not b, v)) == not (eval_nnf sigma (NNFLit (b, v)))
  sigma (not b) v == not (sigma b v)  

  2. 
  zalozmy ze zachodzi dla f1,f2
  f = NNFConj (f1, f2)
  eval_nnf sigma (neg_nnf (NNFConj (f1, f2))) == not (eval_nnf sigma (NNFConj (f1, f2)))
  eval_nnf sigma (NNFDisj (neg_nnf f1, neg_nnf f2)) == not (eval_nnf sigma (NNFConj (f1, f2)))
  eval_nnf sigma (NNFDisj (neg_nnf f1, neg_nnf f2)) == not (eval_nnf sigma f1 && eval_nnf sigma f2)
  eval_nnf sigma (NNFDisj (neg_nnf f1, neg_nnf f2)) == not (eval_nnf sigma f1) || not (eval_nnf sigma f2)
  eval_nnf sigma (neg_nnf f1) || eval_nnf sigma (neg_nnf f2) == not (eval_nnf sigma f1) || not (eval_nnf sigma f2)
  not (eval_nnf sigma f1) || not (eval_nnf sigma f2) == not (eval_nnf sigma f1) || not (eval_nnf sigma f2)

  f = NNFDisj (f1, f2)
  eval_nnf sigma (neg_nnf (NNFDisj (f1, f2))) == not (eval_nnf sigma (NNFDisj (f1, f2)))
  eval_nnf sigma (NNFConj (neg_nnf f1, neg_nnf f2)) == not (eval_nnf sigma (NNFDisj (f1, f2)))
  eval_nnf sigma (neg_nnf f1) && eval_nnf sigma (neg_nnf f2) == not ((eval_nnf sigma f1) || (eval_nnf sigma f2))
  not (eval_nnf sigma f1) && not (eval_nnf sigma f2) == not (eval_nnf sigma f1) && not (eval_nnf sigma f2)
  
*)