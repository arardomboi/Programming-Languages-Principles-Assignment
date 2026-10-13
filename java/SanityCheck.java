import java.util.Map;
import java.util.HashMap;

public class SanityCheck {
    public static void main(String[] args) {
        System.out.println("[Java] Verifying API Contract...");

        // Setup Environment
        Map<String, Integer> env = new HashMap<>();
        env.put("x", 5);

        // Constructor & Interface Compliance
        Expr num = new Num(3);
        Expr var = new Var("x");
        Expr add = new Add(var, num);
        Expr mul = new Mul(add, new Num(2));

        // String Formatting Check
        String str = mul.toString();
        if (!str.equals("((x + 3) * 2)")) {
            System.err.println("FAILED: toString() output incorrect.");
            System.err.println("Expected: ((x + 3) * 2)");
            System.err.println("Actual:   " + str);
            System.exit(1);
        }

        // Evaluation Check
        int val = mul.eval(env);
        if (val != 16) {
            System.err.println("FAILED: eval() returned " + val + " (Expected 16)");
            System.exit(1);
        }

        // Simplification Signature Check
        Expr simp = new Add(new Num(0), var).simplify();

        System.out.println(" PASSED: Java API contract verified successfully.");
    }
}
