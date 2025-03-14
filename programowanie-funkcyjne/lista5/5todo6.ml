type 'a dllist = 'a dllist_data lazy_t
and 'a dllist_data =
  {  prev : 'a dllist
  ; elem : 'a
  ;  next : 'a dllist
  }

let prev = function lazy({ prev; elem; next})-> prev

let elem = function lazy({prev; elem; next}) -> elem

let next_f = function lazy({prev; elem; next}) -> next

let rec of_list xs =
  let rec dll =    
    lazy (
    {
      elem = List.hd xs;
      next = make_next (List.tl xs) dll;
      prev = make_prev dll dll
    }
  )
  and make_prev dll ac =
    if (Lazy.force ac).next == dll then
      ac
    else make_prev dll (Lazy.force ac).next
  and make_next xs prev =
    match xs with
    | [] -> dll
    | x::xs' -> let rec actual = lazy ( 
      {
        prev = prev;
        elem = x;
        next = make_next xs' actual
      }
    ) in actual
  in dll




  let rec make_dllist n =
    let rec current = lazy (
      { prev = make_prev current (n - 1)
      ; elem = n
      ; next = make_next current (n + 1)
      }
    )
    and make_prev next_val n = 
      let rec curr = lazy (
      { prev = make_prev (curr) (n - 1)
      ; elem = n
      ; next = next_val
      }
    ) in curr
    and make_next prev_val n =
      let rec curr = lazy (
      { prev = prev_val
      ; elem = n
      ; next = make_next curr (n + 1)
      }
    )
    in curr
    in current

let integers = make_dllist 0