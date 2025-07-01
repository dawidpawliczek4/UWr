type 'v nnf =
  | NNFLit of bool * 'v
  | NNFConj of 'v nnf * 'v nnf 
  | NNFDisj of 'v nnf * 'v nnf


let rec neg_nnf = function
  | NNFLit (b, v) -> NNFLit (not b, v)
  | NNFConj (f1, f2) -> NNFDisj (neg_nnf f1, neg_nnf f2)
  | NNFDisj (f1, f2) -> NNFConj (neg_nnf f1, neg_nnf f2)

(* 
  dowod ze neg_nnf (neg_nnf f) = f  
  1. baza indukcyjna
    f = NNFLit (b, v)
    neg_nnf (neg_nnf f) = neg_nnf (neg_nnf (NNFLit (b, v))) = neg_nnf (NNFLit (not b, v)) = NNFLit (b, v) = f
  2. krok indukcyjny
  wezmy dowolne f1, f2, zalozmy ze zachodzi dla nich ze neg_nnf (neg_nnf f1) = f1 i neg_nnf (neg_nnf f2) = f2
  pokazmy, ze zachodzi dla f = NNFConj (f1, f2) i f = NNFDisj (f1, f2)

    f = NNFConj (f1, f2)
    neg_nnf (neg_nnf f) = neg_nnf (neg_nnf (NNFConj (f1, f2))) = neg_nnf (NNFDisj (neg_nnf f1, neg_nnf f2)) = NNFConj (neg_nnf (neg_nnf f1), neg_nnf (neg_nnf f2)) = NNFConj (f1, f2) = f

    f = NNFDisj (f1, f2)
    neg_nnf (neg_nnf f) = neg_nnf (neg_nnf (NNFDisj (f1, f2))) = neg_nnf (NNFConj (neg_nnf f1, neg_nnf f2)) = NNFDisj (neg_nnf (neg_nnf f1), neg_nnf (neg_nnf f2)) = NNFDisj (f1, f2) = f
*)