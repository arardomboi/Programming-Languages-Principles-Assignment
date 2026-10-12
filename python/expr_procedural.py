from typing import Dict, Union
 
# --- DATA STRUCTURES ---
class Num:
   def __init__(self, value: int):
       self.value = value
 
# TODO: Define Var, Add, Mul
 
# Type aliases for annotations
Expr = Union[Num, 'Var', 'Add', 'Mul']
Env = Dict[str, int]
 
# --- PROCEDURES --- 
def eval_expr(expr: Expr, env: Env) -> int:
   """Evaluates an expression tree given a variable mapping environment."""
   raise NotImplementedError("TODO: Implement eval_expr")
 
def to_string(expr: Expr) -> str:
   """Returns a fully-parenthesized string representation of the expression tree."""
   raise NotImplementedError("TODO: Implement to_string")
 
def simplify(expr: Expr) -> Expr:
   """Recursively simplifies expressions applying zero and identity rules."""
   raise NotImplementedError("TODO: Implement simplify")