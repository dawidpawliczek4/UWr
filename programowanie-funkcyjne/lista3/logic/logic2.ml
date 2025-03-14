type formula =
  | Impl of formula * formula
  | False
  | Var of string

let rec string_of_formula f =
  match f with 
  | Var v -> v
  | False -> "⊥"
  | Impl (f1, f2) ->
    let f1_string = string_of_formula f1 in
    let f2_string = string_of_formula f2 in
    begin
    match f1 with
    | Impl _ ->
      "(" ^ f1_string ^ ") -> " ^ f2_string
      | _ ->  f1_string ^ " -> " ^ f2_string
    end


(* #install_printer pp_print_formula;; *)

let f1 = Var "p"
let f2 = Impl (Var "p", Var "q")
let f3 = Impl (Var "p", Impl (Var "q", Var "r"))
let f4 = Impl (Impl (Var "p", Var "q"), Var "r")
let f5 = Impl (Var "p", False)


let pp_print_formula fmtr f =
  Format.pp_print_string fmtr (string_of_formula f)

type theorem = { assumptions: formula list; consequence: formula }

let rec assumptions thm = thm.assumptions

let rec consequence thm = thm.consequence
  

let pp_print_theorem fmtr thm =
  let open Format in
  pp_open_hvbox fmtr 2;
  begin match assumptions thm with
  | [] -> ()
  | f :: fs ->
    pp_print_formula fmtr f;
    fs |> List.iter (fun f ->
      pp_print_string fmtr ",";
      pp_print_space fmtr ();
      pp_print_formula fmtr f);
    pp_print_space fmtr ()
  end;
  pp_open_hbox fmtr ();
  pp_print_string fmtr "⊢";
  pp_print_space fmtr ();
  pp_print_formula fmtr (consequence thm);
  pp_close_box fmtr ();
  pp_close_box fmtr ()

let by_assumption f =
  { assumptions = [f]; consequence = f}
  

let imp_i f thm =
    let new_assumptions = List.filter ((<>) f) thm.assumptions in
    { assumptions = new_assumptions; consequence = Impl (f, thm.consequence) }
  

let imp_e th1 th2 = 
  match th1.consequence with
  | Impl(f1, f2) when f1 = th2.consequence ->
      { assumptions = th1.assumptions @ th2.assumptions; consequence=f2}
  | _ -> failwith "Nieprawidłowy dowód: pierwsza część nie jest implikacją lub przesłanki nie pasują"
  

let bot_e f thm = 
  if thm.consequence = False
  then { assumptions = thm.assumptions; consequence=f} 
  else failwith "Nieprawidłowy dowód: dowód nie zawiera ⊥"

