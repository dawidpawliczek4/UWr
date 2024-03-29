module type DICT = sig
  type key
  type 'a dict
  val empty : 'a dict
  val insert : key -> 'a -> 'a dict -> 'a dict
  val remove : key -> 'a dict -> 'a dict
  val find_opt : key -> 'a dict -> 'a option
  val find : key -> 'a dict -> 'a
  val to_list : 'a dict -> (key * 'a) list
end


module MakeListDict (Order: Map.OrderedType): DICT with type key = Order.t = struct
  type key = Order.t
  type 'a dict = (key * 'a) list
  let empty = []
  let insert k v d = (k, v) :: d
  let remove k d = List.filter (fun (k', _) -> Order.compare k k' <> 0) d  
  let find_opt k d = List.find_opt (fun (k', _) -> Order.compare k k' = 0) d |> Option.map snd
  let find k d = List.find (fun (k', _) -> Order.compare k k' = 0) d |> snd
  let to_list d = d
end

module CharListDict = MakeListDict(Char)


(* zad 4 *)


module MakeMapDict (Order: Map.OrderedType) : (DICT with type key = Order.t) = struct
  module M = Map.Make(Order)
  type key = M.key
  type 'a dict = 'a M.t
  let empty = M.empty
  let insert = M.add
  let remove = M.remove
  let find_opt = M.find_opt
  let find = M.find
  let to_list = M.bindings
end

module CharMapDict = MakeMapDict(Char)