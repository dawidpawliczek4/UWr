type sock
type ans

val output_string : sock -> string -> (unit -> ans) -> ans

val input_line : sock -> (string option -> ans) -> ans

val close : sock -> ans

val establish_server : port:int -> (sock -> ans) -> unit
