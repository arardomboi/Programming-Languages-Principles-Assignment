-- Imports
module Expr where

import Data.Map (Map)
import qualified Data.Map as Map

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
simplify(Add e1 e2) = simplifyAdd (simplify e1) (simplify e2) -- recursively simplify children
  where
    simplifyAdd (Num 0) e = e -- 0 + e = e
    simplifyAdd e (Num 0) = e -- e + 0 = e
    simplifyAdd s1 s2     = Add s1 s2

simplify(Mul e1 e2) = simplifyMul (simplify e1) (simplify e2) -- recursively simplify children
  where
    simplifyMul (Num 1) e = e -- 1 x e = e
    simplifyMul e (Num 1) = e -- e x 1 = e
    simplifyMul (Num 0) _ = Num 0 -- 0 x e = 0
    simplifyMul _ (Num 0) = Num 0 -- e x 0 = 0
    simplifyMul s1 s2     = Mul s1 s2