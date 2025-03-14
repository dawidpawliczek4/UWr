module type OrderedType = sig
  type t
  val compare : t -> t -> int
end

module Make(Key:OrderedType) = struct 
  module P = Perm.Make(Key)
  module S = Set.Make(P)

  type p = P.t

  let rec aux p curr prev =
    if S.equal curr prev then false else
      let inverted = S.fold (fun perm acc -> S.add (P.invert perm) acc) curr S.empty in
      let composed = S.fold ......

  let is_generated p g = 
    aux p (S.add P.id ........)
  end
  