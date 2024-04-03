// Bazowy interfejs lub klasa abstrakcyjna dla wszystkich wyrażeń

import java.util.HashMap;
import java.util.Map;

abstract class Expression {
    public abstract int evaluate();

    public abstract String toString();
}

// Reprezentuje stałą wartość w wyrażeniu
class Const extends Expression {
    private int value;

    public Const(int value) {
        this.value = value;
    }

    public int evaluate() {
        return value;
    }

    public String toString() {
        return Integer.toString(value);
    }
}

class Context {
    private Map<String, Integer> variables;

    public Context() {
        variables = new HashMap<>();
    }

    public void setValue(String name, int value) {
        variables.put(name, value);
    }

    public int getValue(String name) {
        if (variables.containsKey(name)) {
            return variables.get(name);
        } else {
            throw new IllegalArgumentException("Variable " + name + " not found in the context");
        }
    }
}

// Reprezentuje zmienną w wyrażeniu
class Variable extends Expression {
    private String name;
    private Context context;

    public Variable(String name, Context context) {
        this.name = name;
        this.context = context;
    }

    public void changeContext (Context context) {
        this.context = context;
    }

    public int evaluate() {
        return context.getValue(name);
    }

    public String toString() {
        return name;
    }
}

// Reprezentuje operację dodawania
class Add extends Expression {
    private Expression left;
    private Expression right;

    public Add(Expression left, Expression right) {
        this.left = left;
        this.right = right;
    }

    public int evaluate() {
        return left.evaluate() + right.evaluate();
    }

    public String toString() {
        return "(" + left.toString() + " + " + right.toString() + ")";
    }
}

// Reprezentuje operację odejmowania
class Subtract extends Expression {
    private Expression left;
    private Expression right;

    public Subtract(Expression left, Expression right) {
        this.left = left;
        this.right = right;
    }

    public int evaluate() {
        return left.evaluate() - right.evaluate();
    }

    public String toString() {
        return "(" + left.toString() + " - " + right.toString() + ")";
    }
}

public class Program {
    public static void main(String[] args) {
        // 2 + 3 = 5
        Expression e1 = new Add(new Const(2), new Const(3));
        System.out.println(e1 + " = " + e1.evaluate());

        // 2 + 3 - 4 = 1
        Expression e2 = new Subtract(e1, new Const(4));
        System.out.println(e2 + " = " + e2.evaluate());

        // 17 + 23 - 44 = -4
        Expression e3 = new Subtract(new Add(new Const(17), new Const(23)), new Const(44));
        System.out.println(e3 + " = " + e3.evaluate());

        // x = 5
        Context context = new Context();
        context.setValue("x", 5);
        Expression e4 = new Variable("x", context);
        System.out.println(e4 + " = " + e4.evaluate());
    }

}