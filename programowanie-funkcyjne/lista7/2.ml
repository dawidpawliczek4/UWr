module type RandomMonad = sig
  type 'a t
  val return : 'a -> 'a t
  val bind   : 'a t -> ('a -> 'b t) -> 'b t  
  val random : int t
  val run : int -> 'a t -> 'a
end


module RS: sig include RandomMonad end = 
struct
  type 'a t = int -> 'a * int
  let return x = fun st -> (x, st)

  let bind m f = fun st ->
    let (x, new_st) = m st in
    f x new_st

    let next_seed seed =
      let a = 16807 in
      let m = 2147483647 in
      let q = 127773 in
      let r = 2836 in
      let hi = seed / q in
      let lo = seed mod q in
      let b = a * lo - r * hi in
      if b > 0 then b else b + m

  let random = fun seed ->
    let new_seed = next_seed seed in
    let rand = new_seed in
    (rand, new_seed)

  let run: int -> 'a t -> 'a =
   fun seed m ->
    let (result, _) = m seed in result
end