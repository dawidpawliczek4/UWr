module type Monad = sig
  type 'a t
  val return : 'a -> 'a t
  val bind   : 'a t -> ('a -> 'b t) -> 'b t
end

module Err : sig
include Monad
val fail : 'a t
val catch : 'a t -> (unit -> 'a t) -> 'a t 
val run :'a t -> 'a option
end = struct
  type 'a t
  let return x = failwith ""
  let bind  x y= failwith ""
  let fail = failwith ""
  let catch x y = failwith ""
  let run x = failwith ""
end

module BT : sig
  include Monad
  val fail : 'a t
  val flip : bool t
  valrun :'at->'aSeq.t
end = struct
  
end

module St(State : sig type t end) : sig
  include Monad
  val get : State.t t
  val set : State.t -> unit t
  val run : State.t -> 'a t -> 'a
end = struct
  
end