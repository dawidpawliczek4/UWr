(* abstract syntax tree *)
type bop = Mult | Div | Add | Sub | Eq | Lt | Gt | Leq | Geq | Neq | And | Or
type ident = string                                                      
type expr =
  | Int of int
  | Bool of bool
  | Var of ident
  | Binop of bop * expr * expr
  | If of expr * expr * expr
  | Let of ident * expr * expr


type variable = string
type range = int * int
type expression = 
  | Variable of variable
  | Int of int
  | Plus of expression * expression
  | Minus of expression * expression
  | Times of expression * expression
  | Divide of expression * expression
  (* Definicje dalszych operacji ... *)

type statement =
  | ForLoop of variable * range * statement list
  | ComputeIntegral of variable * range * expression
  (* Definicje dalszych instrukcji ... *)
