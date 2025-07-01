open Logic

type goal = (string * formula) list * formula

type incomplete_proof =   
| Goal of      goal
| ImplIntro of goal * incomplete_proof
| ImplElim of  goal * goal * incomplete_proof
| FalseElim of goal * incomplete_proof
| Complete of  theorem

type context  =
 | Root
 | ImplIntroCtx of     context * incomplete_proof 
 | ImplElimLeft of  context * incomplete_proof
 | ImplElimRight of context * incomplete_proof
 | FalseElimCtx of     context * incomplete_proof

type proof =
   | Complete of theorem
   | Incomplete of context * incomplete_proof 

let proof g f =
  Incomplete(Root, Goal(g, f))

let qed pf =
  match pf with
  | Incomplete(_, Complete thm) -> thm
  | _ -> failwith "Invalid proof"

let goal pf =
  match pf with
  | Complete  _-> None
  | Incomplete(_, Goal(g,f)) -> Some(g, f)
  | _ -> failwith "Invalid proof"

let next pf =
  (* TODO: zaimplementuj *)
  failwith "not implemented"

let intro (name: string) pf =
  match pf with
  | Incomplete(ctx, Goal(g, Impl(fi, psi)))->   
    let new_goal = ((name, fi) :: g, psi) in 
    (* Incomplete(ImplIntroCtx(ctx, ImplIntro(new_goal, Goal(g, Impl(fi, psi)))), Goal(new_goal)) *)
    Incomplete(ctx, ImplIntro(new_goal, Goal(g, Impl(fi,psi))))
  | _ -> failwith "Invalid proof"

let apply f pf =
  (* TODO: zaimplementuj *)
  failwith "not implemented"

let apply_thm thm pf =
  (* TODO: zaimplementuj *)
  failwith "not implemented"

let apply_assm name pf =
  (* TODO: zaimplementuj *)
  failwith "not implemented"

let pp_print_proof fmtr pf =
  match goal pf with
  | None -> Format.pp_print_string fmtr "No more subgoals"
  | Some(g, f) ->
    Format.pp_open_vbox fmtr (-100);
    g |> List.iter (fun (name, f) ->
      Format.pp_print_cut fmtr ();
      Format.pp_open_hbox fmtr ();
      Format.pp_print_string fmtr name;
      Format.pp_print_string fmtr ":";
      Format.pp_print_space fmtr ();
      pp_print_formula fmtr f;
      Format.pp_close_box fmtr ());
    Format.pp_print_cut fmtr ();
    Format.pp_print_string fmtr (String.make 40 '=');
    Format.pp_print_cut fmtr ();
    pp_print_formula fmtr f;
    Format.pp_close_box fmtr ()