import java.util.Map;
import java.util.Objects;

// Interface
public interface Expr {
    int eval(Map<String, Integer> env);

    String toString();

    Expr simplify();
}

// Num
class Num implements Expr {
    private final int value;

    public Num(int value) {
        this.value = value;
    }

    public int getValue() {
        return value;
    }

    // Helper: is e a Num with the given value?
    static boolean is(Expr e, int v) {
        return e instanceof Num && ((Num) e).value == v;
    }

    @Override
    public int eval(Map<String, Integer> env) {
        return value;
    }

    @Override
    public String toString() {
        return Integer.toString(value);
    }

    @Override
    public Expr simplify() {
        return this;
    }

    @Override
    public boolean equals(Object obj) {
        return obj instanceof Num && ((Num) obj).value == value;
    }

    @Override
    public int hashCode() {
        return Integer.hashCode(value);
    }
}

// Variable
class Var implements Expr {
    private final String name;

    public Var(String name) {
        this.name = name;
    }

    public String getName() {
        return name;
    }

    @Override
    public int eval(Map<String, Integer> env) {
        if (env == null || !env.containsKey(name)) {
            throw new IllegalArgumentException("Unbound variable: " + name);
        }
        return env.get(name);
    }

    @Override
    public String toString() {
        return name;
    }

    @Override
    public Expr simplify() {
        return this;
    }

    @Override
    public boolean equals(Object obj) {
        return obj instanceof Var && Objects.equals(((Var) obj).name, name);
    }

    @Override
    public int hashCode() {
        return Objects.hashCode(name);
    }
}

// Addition
class Add implements Expr {
    private final Expr left;
    private final Expr right;

    public Add(Expr left, Expr right) {
        this.left = left;
        this.right = right;
    }

    public Expr getLeft() {
        return left;
    }

    public Expr getRight() {
        return right;
    }

    @Override
    public int eval(Map<String, Integer> env) {
        return left.eval(env) + right.eval(env);
    }

    @Override
    public String toString() {
        return "(" + left + " + " + right + ")";
    }

    @Override
    public Expr simplify() {
        // Bottom-up recursion
        Expr l = left.simplify();
        Expr r = right.simplify();

        if (Num.is(l, 0)) return r; // 0 + e -> e
        if (Num.is(r, 0)) return l; // e + 0 -> e
        return new Add(l, r);
    }

    @Override
    public boolean equals(Object obj) {
        if (!(obj instanceof Add)) return false;
        Add other = (Add) obj;
        return left.equals(other.left) && right.equals(other.right);
    }

    @Override
    public int hashCode() {
        return Objects.hash("Add", left, right);
    }
}

// Multiplication
class Mul implements Expr {
    private final Expr left;
    private final Expr right;

    public Mul(Expr left, Expr right) {
        this.left = left;
        this.right = right;
    }

    public Expr getLeft() {
        return left;
    }

    public Expr getRight() {
        return right;
    }

    @Override
    public int eval(Map<String, Integer> env) {
        return left.eval(env) * right.eval(env);
    }

    @Override
    public String toString() {
        return "(" + left + " * " + right + ")";
    }

    @Override
    public Expr simplify() {
        // Bottom-up recursion
        Expr l = left.simplify();
        Expr r = right.simplify();

        if (Num.is(l, 0) || Num.is(r, 0)) return new Num(0); // 0 * e, e * 0 -> 0
        if (Num.is(l, 1)) return r;                          // 1 * e -> e
        if (Num.is(r, 1)) return l;                          // e * 1 -> e
        return new Mul(l, r);
    }

    @Override
    public boolean equals(Object obj) {
        if (!(obj instanceof Mul)) return false;
        Mul other = (Mul) obj;
        return left.equals(other.left) && right.equals(other.right);
    }

    @Override
    public int hashCode() {
        return Objects.hash("Mul", left, right);
    }
}