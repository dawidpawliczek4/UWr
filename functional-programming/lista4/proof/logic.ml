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

let f1 = Var "p"
let f2 = Impl (Var "p", Var "q")
let f3 = Impl (Var "p", Impl (Var "q", Var "r"))
let f4 = Impl (Impl (Var "p", Var "q"), Var "r")
let f5 = Impl (Var "p", False)


let pp_print_formula fmtr f =
  Format.pp_print_string fmtr (string_of_formula f)

type theorem =
  | Assumption of formula list * formula
  | ImplIntro of theorem * formula list * formula
  | ImplElim of theorem * theorem * formula list * formula
  | FalseElim of theorem * formula list * formula

let rec assumptions thm =
  match thm with
  | Assumption (fl, f) -> fl
  | ImplIntro (t, fl, f) -> fl
  | ImplElim (t1, t2, fl, f) -> fl
  | FalseElim (t, fl, f) -> fl

let rec consequence thm =
  match thm with
  | Assumption (fl, f) -> f
  | ImplIntro (t, fl, f) -> f
  | ImplElim (t1, t2, fl, f) -> f
  | FalseElim (t, fl, f) -> f
  

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
  Assumption ([f], f)

let imp_i f thm =
  let new_assumptions = List.filter ((<>) f) (assumptions thm) in
  ImplIntro(thm, new_assumptions, Impl(f, consequence thm))

let imp_e th1 th2 =
  match (consequence th1) with
  | Impl(f1,f2) when f1 = (consequence th2) ->
    ImplElim(th1, th2, assumptions th1 @ assumptions th2, f2)
  | _ -> failwith "Nieprawidłowy dowód: pierwsza część nie jest implikacją lub przesłanki nie pasują"

let bot_e f thm =
  if consequence thm = False
  then FalseElim(thm, assumptions thm, f)
  else failwith "Nieprawidłowy dowód: dowód nie zawiera ⊥"



(* let proof1 = 
  let p = Var "p" in
  imp_i p (by_assumption p)

let proof2 = 
  let p = Var "p" in let q = Var "q" in
  imp_i p (imp_i q (by_assumption p))

let proof3 = 
  let p = Var "p" in let q = Var "q" in let r = Var "r" in
  imp_i p (imp_i q (imp_i r (by_assumption p)))

let proof4 = 
  let p = Var "p" in
  imp_i False (bot_e p (by_assumption False)) *)