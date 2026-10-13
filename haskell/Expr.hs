-- Imports
module AST where
    import Data.Map (Map)
    import qualified Data.Map as Map

module Expr where
 
data Expr
    = Num Int 
    | Var String 
    | Add Expr Expr 
    | Mul Expr Expr 
    deriving (Show, Eq)

type Env = [(String, Int)]
 
-- Function Stubs: Implement using pattern matching and recursion
eval :: Env -> Expr -> Int
eval env (Num n) = n --input is a number, return it
eval env (Var v) = case lookup v env of --input is a variable, look it up in the environment
    Just n -> n
    Nothing -> error $ "Variable " ++ v ++ " not found in environment."
eval env (Add e1 e2) = eval env e1 + eval env e2 -- input is an addition, evaluate both sides recursively and return the sum
eval env (Mul e1 e2) = eval env e1 * eval env e2 -- input is a multiplication, evaluate both sides recursively and return the product
 
toString :: Expr -> String --Converts the AST to a string representation
toString(Num n) = show n
toString(Var v) = v
toString(Add e1 e2) = "(" ++ toString e1 ++ " + " ++ toString e2 ++ ")"
toString(Mul e1 e2) = "(" ++ toString e1 ++ " * " ++ toString e2 ++ ")"
 
simplify :: Expr -> Expr -- Simplifies the AST
simplify(Num n) = Num n -- cant simplify numbers
simplify(Var v) = Var v -- cant simplify variables
simplify(Add (Num 0) e) = simplify e -- 0 + e = e
simplify(Add e (Num 0)) = simplify e -- e + 0 = e
simplify(Add e1 e2) = Add (simplify e1) (simplify e2) -- recursively simplify children
simplify(Mul (Num 1) e) = simplify e -- 1 x e = e
simplify(Mul e (Num 1)) = simplify e -- e x 1 = e
simplify(Mul (Num 0) _) = Num 0 -- 0 x e = 0
simplify(Mul _ (Num 0)) = Num 0 -- e x 0 = 0
simplify(Mul e1 e2) = Mul (simplify e1) (simplify e2) -- recursively simplify children
