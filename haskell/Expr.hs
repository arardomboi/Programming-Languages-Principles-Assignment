module Expr where
 
data Expr
    = Num Int 
    | Var String 
    | Add Expr Expr 
    | Mul Expr Expr 
    deriving (Show, Eq)

-- Environment definition for variable lookups
type Env = [(String, Int)]
 
-- Function Stubs: Implement using pattern matching and recursion
eval :: Env -> Expr -> Int
eval = error "TODO: Implement eval"
 
toString :: Expr -> String
toString = error "TODO: Implement toString"
 
simplify :: Expr -> Expr
simplify = error "TODO: Implement simplify"