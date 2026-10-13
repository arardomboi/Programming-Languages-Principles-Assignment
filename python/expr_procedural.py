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

def eval_expr(expr: Expr, env: Env) -> int:
    simplified_expr = simplify(expr)  # Simplify the expression first


    if isinstance(simplified_expr, Num): #return its value
        return simplified_expr.value
    elif isinstance(simplified_expr, Var): #return its value
        if simplified_expr.name in env:
            return env[simplified_expr.name]
        else:
            raise ValueError(f"Variable '{simplified_expr.name}' not found in environment.")
    elif isinstance(simplified_expr, Add): #recursively evaluate its left and right children and return their sum
        return eval_expr(simplified_expr.left, env) + eval_expr(simplified_expr.right, env)
    elif isinstance(simplified_expr, Mul): #recursively evaluate its left and right children and return their product
        return eval_expr(simplified_expr.left, env) * eval_expr(simplified_expr.right, env)
    raise ValueError("Invalid expression type")
        
 
def to_string(expr: Expr) -> str:
    """Converts an expression tree into a human-readable, fully-parenthesized string."""
    if isinstance(expr, Num): #converts number to string
        return str(expr.value)
    elif isinstance(expr, Var): #variable already a string, so return the name
        return expr.name
    elif isinstance(expr, Add): #recursively call to_string on left and right children of Add node and format as "(left + right)"
        return f"({to_string(expr.left)} + {to_string(expr.right)})"
    elif isinstance(expr, Mul): #same logic as Add, but for multiplication
        return f"({to_string(expr.left)} * {to_string(expr.right)})"
    raise ValueError("Invalid expression type")

def simplify(expr: Expr) -> Expr:
    """Simplifies an expression tree according to the specified algebraic rules."""
    # Base Case: Constants and variables cannot be simplified further
    if isinstance(expr, (Num, Var)):
        return expr

    # Bottom-Up Recursion
    left_simp = simplify(expr.left)
    right_simp = simplify(expr.right)

    # Apply simplification rules for Add
    if isinstance(expr, Add):
        # 0 + e -> e
        if isinstance(left_simp, Num) and left_simp.value == 0:
            return right_simp
        # e + 0 -> e
        if isinstance(right_simp, Num) and right_simp.value == 0:
            return left_simp
        
        # If no rules match, return the node with its simplified children
        return Add(left_simp, right_simp)
        
    # Apply simplification rules for Mul
    elif isinstance(expr, Mul):
        # 0 * e -> 0 or e * 0 -> 0
        if (isinstance(left_simp, Num) and left_simp.value == 0) or \
           (isinstance(right_simp, Num) and right_simp.value == 0):
            return Num(0)
            
        # 1 * e -> e
        if isinstance(left_simp, Num) and left_simp.value == 1:
            return right_simp
        # e * 1 -> e
        if isinstance(right_simp, Num) and right_simp.value == 1:
            return left_simp
            
        # If no rules match, return the node with its simplified children
        return Mul(left_simp, right_simp)
        
    else:
        raise ValueError("Invalid expression type")
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