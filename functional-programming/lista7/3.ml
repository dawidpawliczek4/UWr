module Ident = struct 

  type 'a t = 'a

  let return : 'a -> 'a t =
     fun x -> x

  let bind :  'a t -> ('a -> 'b t) -> 'b t =
  fun m f -> f m


end


module LazyIdent = struct
  
  type 'a t = unit -> 'a

  let return : 'a -> 'a t =
    fun x -> fun () -> x

  let bind: 'a t -> ('a -> 'b t) -> 'b t =
  fun m f ->
    let unlazy =  m () in
    f unlazy


  let bind2: 'a t -> ('a -> 'b t) -> 'b t  =
    fun m f ->
      fun () ->
      let unlazy = m () in
      let next_lazy = f unlazy in
      next_lazy ()

end