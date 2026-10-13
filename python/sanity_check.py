import sys
from expr_procedural import Num, Var, Add, Mul, eval_expr, to_string, simplify


def run_sanity_check():
    print("[Python] Verifying API Contract...")
    env = {"x": 5}

    # Verify Class Constructors
    ast = Mul(Add(Var("x"), Num(3)), Num(2))

    # Verify String Formatting Procedure
    str_val = to_string(ast)
    if str_val != "((x + 3) * 2)":
        print(f"FAILED: to_string() returned '{str_val}' (Expected '((x + 3) * 2)')", file=sys.stderr)
        sys.exit(1)

    # Verify Evaluation Procedure
    eval_val = eval_expr(ast, env)
    if eval_val != 16:
        print(f"FAILED: eval_expr() returned {eval_val} (Expected 16)", file=sys.stderr)
        sys.exit(1)

    # Verify Simplification Procedure Signature
    simp = simplify(Add(Num(0), Var("x")))

    print(" PASSED: Python API contract verified successfully.")


if __name__ == "__main__":
    run_sanity_check()
