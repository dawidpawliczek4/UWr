
(* PLIK AST.ML *)

type bop = Mult | Div | Add | Sub | Eq (* + *) | Ls | LsEq | Gr | GrEq | Ineq

(* PLIK LEXER.MLL *)

rule read =
  parse
  | white { read lexbuf }
  | "=" { EQ }
  (* + *)
  | "<" { LS }
  | "<=" { LSEQ }
  | ">" { GR }
  | ">=" { GREQ }
  | "<>" { INEQ }

  | "true" { TRUE }
  | "false" { FALSE }
  | "if" { IF }
  | "then" { THEN }
  | "else" { ELSE }
  | "*" { TIMES }
  | "+" { PLUS }
  | "-" { MINUS }
  | "/" { DIV }
  | "(" { LPAREN }
  | ")" { RPAREN }
  | number { INT (int_of_string (Lexing.lexeme lexbuf)) } 
  | eof { EOF }



(* (PLIK PARSER.MLY) *)

%{
open Ast
%}

%token <int> INT
%token TIMES
%token DIV
%token PLUS
%token MINUS
%token LPAREN
%token RPAREN
%token EQ
(*  *)
%token LS
%token LSEQ
%token GR
%token GREQ
%token INEQ
(*  *)
%token TRUE
%token FALSE
%token IF
%token THEN
%token ELSE
%token EOF

expr:
  | i = INT { Int i }
  | e1 = expr; PLUS; e2 = expr { Binop(Add, e1, e2) }
  | e1 = expr; MINUS; e2 = expr { Binop(Sub, e1, e2) }
  | e1 = expr; DIV; e2 = expr { Binop(Div, e1, e2) }
  | e1 = expr; TIMES; e2 = expr { Binop(Mult, e1, e2) }
  | LPAREN; e = expr; RPAREN { e }
  | TRUE { Bool true }
  | FALSE { Bool false }
  | e1 = expr; EQ; e2 = expr { Binop(Eq, e1, e2) }
  (*  *)
  | e1 = expr; LS; e2 = expr { Binop(Ls, e1, e2) }
  | e1 = expr; LSEQ; e2 = expr { Binop(LsEq, e1, e2) }
  | e1 = expr; GR; e2 = expr { Binop(Gr, e1, e2) }
  | e1 = expr; GREQ; e2 = expr { Binop(GrEq, e1, e2) }
  | e1 = expr; INEQ; e2 = expr { Binop(Ineq, e1, e2) }
(*  *)
  | IF; e1 = expr; THEN; e2 = expr; ELSE; e3 = expr { If(e1, e2, e3) }
  ;



(* (PLIK MAIN.ML) *)

let eval_op (op : bop) (v1 : value) (v2 : value) : value =
  match op, v1, v2 with
  | Add,  VInt i1, VInt i2 -> VInt (i1 + i2)
  | Sub,  VInt i1, VInt i2 -> VInt (i1 - i2)
  | Mult, VInt i1, VInt i2 -> VInt (i1 * i2)
  | Div,  VInt i1, VInt i2 -> VInt (i1 / i2)
  | Eq,   VInt i1, VInt i2 -> VBool (i1 = i2)
  (*  *)
  | Ls,   VInt i1, VInt i2 -> VBool (i1 < i2)
  | LsEq, VInt i1, VInt i2 -> VBool (i1 <= i2)
  | Gr,   VInt i1, VInt i2 -> VBool (i1 > i2)
  | GrEq, VInt i1, VInt i2 -> VBool (i1 >= i2)
  | Ineq, VInt i1, VInt i2 -> VBool (i1 <> i2)
(*  *)
  | _ -> failwith "type error"