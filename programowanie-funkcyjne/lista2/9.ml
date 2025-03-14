
type 'a clist = { clist: 'z. ('a -> 'z -> 'z) -> 'z -> 'z }

let cnil = { clist = fun f z -> z }

let ccons (hd: 'a) (cl: 'a clist) : 'a clist =
  {
    clist = fun f z ->
      f hd (cl.clist f z)
  }


let map callback xs =
  {
    clist = fun f z ->
      xs.clist (fun a acc -> f (callback a) acc) z
  }

let append xs ys =
  {
    clist = fun f z ->
      ys.clist f (xs.clist f z)
  }

let clist_to_list xs =
  xs.clist (fun a acc -> a::acc) []

let rec list_to_clist xs =
  match xs with
  | [] -> cnil
  | x::xs' -> ccons x (list_to_clist xs') 

let rec prod xs ys =
  match (xs, ys) with
  | ([], _) | (_, []) -> []
  | (x :: xs', y :: ys') -> (x, y) :: prod xs' ys'

let prod xs ys =
  {
    clist = fun f z ->
      xs.clist (fun a acc_a -> ys.clist (fun b acc_b -> f (a, b) acc_b) acc_a) z
  }


  
(* let cnth clist n =
  let rec nth_helper count current_element next =
    if count = 0 then current_element
    else next (nth_helper (count - 1))
  in
  clist.clist (nth_helper (n - 1)) (fun _ -> failwith "Lista za krotka") *)

  (* 

'a to typ elementów listy.
'z to dowolny typ, który chcemy uzyskać po przetworzeniu listy.
('a -> 'z -> 'z) to funkcja, którą chcemy zastosować na każdym elemencie listy.
'z to wynikowa wartość po przejściu przez całą listę, jak i rowniez dajemy to do clist jako drugi argument, i to nam wypluwa po przejsciu przez cala liste

*)