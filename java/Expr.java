import java.util.Map; // Core Interface: You must implement this interface across all node classes
 
public interface Expr {
    int eval(Map<String, Integer> env);
    String toString();
    Expr simplify();
}
 
// TODO: Implement concrete classes Num, Var, Add, and Mul implementing Expr.
 
// Example Stub for Add:
public class Add implements Expr {
    // TODO: Define private final fields and constructor signature: Add(Expr left, Expr right)
    @Override
    public int eval(Map<String, Integer> env) {
        throw new UnsupportedOperationException("Not implemented");
    }
 
    @Override
    public String toString() {
        throw new UnsupportedOperationException("Not implemented");
    }
 
    @Override
    public Expr simplify() {
        throw new UnsupportedOperationException("Not implemented");
    }
}