// Dawid Pawliczek, 347081, zadanie 1, lista 5

import java.util.ArrayList;
import java.util.Comparator;
import java.util.List;

class OrderedList<T extends Comparable<T>> {
    private List<T> elements;

    public OrderedList() {
        elements = new ArrayList<>();
    }

    public void add_element(T elem) {
        int index = 0;
        while (index < elements.size() && elements.get(index).compareTo(elem) < 0) {
            index++;
        }
        elements.add(index, elem);
    }

    public T get_first() {
        if (elements.isEmpty()) {
            return null;
        }
        return elements.get(0);
    }

    public String toString() {
        return elements.toString();
    }
}

class Card implements Comparable<Card> {
    private int value;

    public Card(int value) {
        this.value = value;
    }

    public int getValue() {
        return value;
    }

    @Override
    public int compareTo(Card other) {
        return Integer.compare(this.value, other.value);
    }

    @Override
    public String toString() {
        return "Card{" +
                "value=" + value +
                '}';
    }
}

class AceCard extends Card {
    public AceCard() {
        super(14); // Wartość Asa najwyższa w wielu grach, więc przyjmujemy 14
    }

    @Override
    public String toString() {
        return "AceCard{}";
    }
}

class KingCard extends Card {
    public KingCard() {
        super(13);
    }

    @Override
    public String toString() {
        return "KingCard{}";
    }
}

class QueenCard extends Card {
    public QueenCard() {
        super(12);
    }

    @Override
    public String toString() {
        return "QueenCard{}";
    }
}

class JackCard extends Card {
    public JackCard() {
        super(11);
    }

    @Override
    public String toString() {
        return "JackCard{}";
    }
}

public class ZadaniePierwsze {
    public static void main(String[] args) {
        OrderedList<Card> cards = new OrderedList<>();
        cards.add_element(new KingCard());     
        cards.add_element(new QueenCard());
        cards.add_element(new AceCard());  
        cards.add_element(new JackCard());         
        System.out.println(cards);
        System.out.println(cards.get_first());        
    }
}