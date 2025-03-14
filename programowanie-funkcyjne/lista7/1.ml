module type RandomMonad = sig
  type 'a t
  val return : 'a -> 'a t
  val bind   : 'a t -> ('a -> 'b t) -> 'b t
  val random : int t
end


module Shuffle(R : RandomMonad) : sig
  val shuffle : 'a list -> 'a list R.t
end = struct 
  let (let*) = R.bind
  let rec extract_at idx lst acc =
    match idx, lst with
    | 0, x :: xs -> (x, List.rev_append acc xs)
    | _, x :: xs -> extract_at (idx - 1) xs (x :: acc)
    | _, [] -> failwith "Index out of bounds"

  let rec shuffle lst =
    match lst with
    | [] -> R.return [] 
    | _ ->
      let* idx = R.random in
      let (x, rest) = extract_at (idx mod (List.length lst)) lst [] in
      let* perm = shuffle rest in
      R.return (x :: perm)
end