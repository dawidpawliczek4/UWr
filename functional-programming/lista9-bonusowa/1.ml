type _ fin_type =
  | Unit : unit fin_type
  | Bool : bool fin_type
  | Pair : 'a fin_type * 'b fin_type -> ('a * 'b) fin_type
;;

let rec all_values : type a. a fin_type -> a Seq.t =
  function
  | Bool -> let t = Seq.cons false (Seq.return true) in t
  | Unit -> Seq.return ()
  | Pair (first, second) -> 
    begin
      let fstSeq = all_values first in
      let sndSeq = all_values second in
      Seq.product fstSeq sndSeq
    end
;;