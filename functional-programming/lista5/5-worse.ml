type 'a dllist = 'a dllist_data lazy_t
and 'a dllist_data =
  { prev : 'a dllist
  ; elem : 'a
  ; next : 'a dllist
  }

let of_list xs =
  let rec make_next xs first prev =
    match xs with
    | [] -> first
    | x :: xs' ->
      let rec current = lazy (
        { prev = prev
        ; elem = x
        ; next = make_next xs' first current
        }
      )
      in current
  in
  match xs with
  | [] -> failwith "List cannot be empty"
  | x :: xs' ->
    let rec first = lazy (
      { prev = make_next (List.rev xs') first first
      ; elem = x
      ; next = make_next xs' first first
      }
    )    
    in first
