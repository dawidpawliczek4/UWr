type _ expr =
  | Const : 'a -> 'a expr
  | App   : ('a -> 'b) expr * 'a expr -> 'b expr

let rec eval : type a. a expr -> a =
  function
  | Const x     -> x
  | App(e1, e2) -> (eval e1) (eval e2)

type _ tp =
  | Int : int tp
  | Arr : 'a tp * 'b tp -> ('a -> 'b) tp

type tc_result =
  | Ok : 'a expr * 'a tp -> tc_result

type (_, _) eq =
  | Refl : ('a, 'a) eq

let rec type_eq : type a b. a tp -> b tp -> (a, b) eq =
  fun tp1 tp2 ->
  match tp1, tp2 with
  | Int, Int -> Refl
  | Int, _   -> failwith "not equal"
  | Arr(a1, b1), Arr(a2, b2) ->
    let Refl = type_eq a1 a2 in
    let Refl = type_eq b1 b2 in
    Refl
  | Arr _, _ -> failwith "not equal"

let rec infer_type : UExpr.t -> tc_result =
  function
  | UInt    n  -> Ok(Const n, Int)
  | UConst "+" -> Ok(Const (+), Arr(Int, Arr(Int, Int)))
  | UConst _   -> failwith "op"
  | UApp(e1, e2) ->
    begin match infer_type e1 with
    | Ok(e1, Int) -> failwith "type error"
    | Ok(e1, Arr(tp2, tp1)) ->
      let (Ok(e2, tp2')) = infer_type e2 in
      let Refl = type_eq tp2 tp2' in
      Ok(App(e1, e2), tp1)
    end
