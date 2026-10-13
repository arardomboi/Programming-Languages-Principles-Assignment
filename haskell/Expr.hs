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
eval = error "TODO: Implement eval"
 
toString :: Expr -> String --Convers the AST to a string representation
toString(Num n) = show n
toString(Var v) = v
toString(Add e1 e2) = "(" ++ toString e1 ++ " + " ++ toString e2 ++ ")"
toString(Mul e1 e2) = "(" ++ toString e1 ++ " * " ++ toString e2 ++ ")"
 
simplify :: Expr -> Expr -- Works expression out
simplify = error "TODO: Implement simplify"