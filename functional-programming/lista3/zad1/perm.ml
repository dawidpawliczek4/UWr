module type OrderedType = sig
    type t
    val compare : t -> t -> int
  end

module type S = sig
    type key
    type t
    (** permutacja jako funkcja *)
    val apply   : t -> key -> key
    
    (** permutacja identycznościowa *)
    val id      : t
    
    (** permutacja odwrotna *)
    val invert :t->t
    
    (** permutacja która tylko zamienia dwa elementy miejscami *)
     val swap : key -> key -> t
    
     (** złożenie permutacji (jako złożenie funkcji) *)
    val compose : t -> t -> t
    
    (** porównywanie permutacji *)
    val compare : t -> t -> int
end


module Make (Key : OrderedType) : S with type key = Key.t = struct
    module KeySet = Set.Make(Key)
    module KeyMap = Map.Make(Key)
    type key = Key.t
    type t = key KeyMap.t * key KeyMap.t 

    (** permutacja jako funkcja *)
    let apply (perm : t) (k : key) : key =
      let (perm, inv) = perm in
      let res = KeyMap.find_opt k perm in
      match res with
      | Some v -> v
      | None -> k
  
    (** permutacja identycznościowa *)
    let id : t =
        (KeyMap.empty, KeyMap.empty)
  
    (** permutacja odwrotna *)
    let invert (perm : t) : t =
      let (perm, inv) = perm in
      (inv, perm) 
  
    (** permutacja która tylko zamienia dwa elementy miejscami *)
    let swap (k1 : key) (k2 : key) : t =
      let perm = KeyMap.add k1 k2 (KeyMap.add k2 k1 KeyMap.empty) in
      let inv = KeyMap.add k2 k1 (KeyMap.add k1 k2 KeyMap.empty) in
      (perm, inv)      
  
    (** złożenie permutacji (jako złożenie funkcji) *)
    (* ??????? *)
    (* 
      perm1 ( perm2 ( x ) )
    *)
    let compose (perm1 : t) (perm2 : t) : t =
      let (perm1, inv1) = perm1 in
      let (perm2, inv2) = perm2 in
      let composed_perm = KeyMap.fold (fun key value acc ->
        match KeyMap.find_opt key perm2 with
        | Some new_key -> KeyMap.add new_key value acc
        | None -> KeyMap.add key value acc
        ) perm1 KeyMap.empty in
        let composed_inv = KeyMap.fold (fun key value acc -> KeyMap.add value key acc) composed_perm KeyMap.empty in
        (composed_perm, composed_inv)

      (*   
    let composed_perm =  KeyMap.fold 
      (fun k v acc ->
          let new_value = apply (perm2, KeyMap.empty) v in
          KeyMap.add k new_value acc
          )
      perm1 
      perm2
     *)
      
  
    (** porównywanie permutacji *)
  let compare ((perm1, _) : t) ((perm2, _) : t) : int =
    KeyMap.compare Key.compare perm1 perm2

end
  