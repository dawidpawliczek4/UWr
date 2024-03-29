// Bazowy interfejs lub klasa abstrakcyjna dla wszystkich wyrażeń
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

// Reprezentuje zmienną w wyrażeniu
class Variable extends Expression {
    private String name;

    public Variable(String name) {
        this.name = name;
    }

    // Załóżmy, że gdzieś istnieje kontekst, który mapuje nazwy zmiennych na ich wartości
    public int evaluate() {
        // tu trzeba by dodać rzeczywisty kod, który pobierze wartość zmiennej z kontekstu
        throw new UnsupportedOperationException("Variables evaluation not implemented yet");
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
    