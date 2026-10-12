from typing import Dict, Union

# --- DATA STRUCTURES ---

class Num:
    def __init__(self, value: int):
        self.value = value

class Var:
    def __init__(self, name: str):
        self.name = name

class Add:
    def __init__(self, left: Expr, right: Expr):
        self.left = left
        self.right = right

class Mul:
    def __init__(self, left: Expr, right: Expr):
        self.left = left
        self.right = right

# Type aliases for annotations
Expr = Union[Num, Var, Add, Mul]
Env = Dict[str, int]

# --- PROCEDURES --- 

def construct_expr(expr_str: str) -> Expr:
    """Build an expression tree representing a given mathematical expression."""
    raise NotImplementedError("TODO: Implement construct_expr")

def eval_expr(expr: Expr, env: Env) -> int:
   """Evaluates an expression tree given a variable mapping environment."""
   raise NotImplementedError("TODO: Implement eval_expr")
 
def to_string(expr: Expr) -> str:
   """Returns a fully-parenthesized string representation of the expression tree."""
   raise NotImplementedError("TODO: Implement to_string")

def simplify(expr: Expr) -> Expr:
    """Simplifies an expression tree according to the specified algebraic rules."""
    #Base Case, cannot simplify futher, i.e. a number of variable
    if isinstance(expr, (Num, Var)):
        return expr

    #Expr is type Add
    if isinstance(expr, Add):
        if expr.left == Num(0):
            return expr.right
        if expr.right == Num(0):
            return expr.left
        
    #Expr is type Mul
    if isinstance(expr, Mul):
        if expr.left == Num(0) or expr.right == Num(0): #If either side is 0, return 0 as e x 0 // 0 x e = 0
            return Num(0)
        if expr.left == Num(1): #If expression is 1 x e, return e 
            return expr.right
        elif expr.right == Num(1): #If expression is e x 1, return e
            return expr.left
    raise NotImplementedError("TODO: Implement simplify")


"""
Core AST Operations
Each solution must support four core operations across all three implementations:
• Construction: Build an expression tree representing a given mathematical expression.
• Evaluation (eval / eval_expr): Evaluate the expression given an environment mapping variable identifiers (e.g., "x", "y") to integer values.
• String Formatting (toString / to_string / print_expr): Convert the expression tree back into a human-readable, fully-parenthesized string with exact spacing (e.g., "(x + (3 * 2))").
• Simplification (simplify / simplify_expr): 
    Recursively apply basic algebraic simplification rules:
    • 0 + e → e and e + 0 → e • 1 × e → e and e × 1 → e • 0 × e → 0 and e × 0 → 0
    • Constant folding (e.g., evaluating 2 + 3 → 5) is NOT required unless one of the operands is 0 or 1 as specified in the rules above. 
    For example, 0 + (2 + 3) → 2 + 3 (Simplifies zero rule, but leaves 2 + 3 as 2 + 3 without folding to 5).

Note: Simplification must operate bottom-up recursively so that nested identities (e.g., (0 * x) + (1 * y)) 
simplify fully to y in a single call. Children must be simplified before evaluating the current node's algebraic 
identities.
"""