type 'a zlist = 'a list * 'a list

let of_list: 'a list -> 'a zlist =
 fun l ->
   ([], l)

let to_list: 'a zlist -> 'a list =
 fun (l1, l2) ->
   List.rev_append l1 l2 

let elem : 'a zlist -> 'a option =
   fun (l1,l2) -> 
    match l2 with
    | [] -> None
    | x::xs -> Some x

let move_left : 'a zlist -> 'a zlist = 
  fun (l1, l2) ->
    match l1 with    
    | x::xs -> (xs, x::l2)
    | [] -> (l1, l2)

let move_right : 'a zlist -> 'a zlist =
  fun (l1, l2) ->    
    match l2 with 
    | x::xs -> (x :: l1, xs)
    | [] -> (l1, l2)

let insert x (l1, l2): 'a zlist = (x::l1, l2)

let remove : 'a zlist -> 'a zlist = 
  fun (l1, l2) ->
    match l1 with
    | x::xs -> (xs, l2)
    | _ -> (l1 ,l2)