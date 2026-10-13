module Main where

import System.Exit (exitFailure)
import Expr (Expr(..), Env, eval, toString, simplify)

main :: IO ()
main = do
  putStrLn "[Haskell] Verifying API Contract..."
  let env :: Env
      env = [("x", 5)]

  -- Construct AST Nodes
  let ast = Mul (Add (Var "x") (Num 3)) (Num 2)

  -- Verify String Formatting
  if toString ast /= "((x + 3) * 2)"
    then do
      putStrLn $ "FAILED: toString output incorrect: " ++ toString ast
      exitFailure
    else return ()

  -- Verify Evaluation
  if eval env ast /= 16
    then do
      putStrLn $ "FAILED: eval returned " ++ show (eval env ast) ++ " (Expected 16)"
      exitFailure
    else return ()

  -- Verify Simplification Signature
  let simp = simplify (Add (Num 0) (Var "x"))

  putStrLn " PASSED: Haskell API contract verified successfully."
