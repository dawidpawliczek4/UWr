// Dawid Pawliczek 347081 lista 6 zadanie 1

import java.util.List;
import java.util.ArrayList;
import java.io.FileOutputStream;
import java.io.FileInputStream;
import java.io.ObjectOutputStream;
import java.io.ObjectInputStream;
import java.io.Serializable;

class OrderedList<T extends Comparable<T>> implements Serializable {
    private static final long serialVersionUID = 1L; // Recommended for Serializable classes
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
        return elements.isEmpty() ? null : elements.get(0);
    }

    @Override
    public String toString() {
        return elements.toString();
    }

    private void writeObject(ObjectOutputStream stream) throws java.io.IOException {
        stream.defaultWriteObject();
    }

    private void readObject(ObjectInputStream stream) throws java.io.IOException, ClassNotFoundException {
        stream.defaultReadObject();
    }

    private void writeObjectNoData() throws java.io.ObjectStreamException {
        // This is typically not implemented unless you have a specific requirement to handle no data states
    }
}

public class First {
    public static void main(String[] args) {
        String filename = "yourfile2.txt";
        try (FileOutputStream fileOut = new FileOutputStream(filename);
             ObjectOutputStream objOut = new ObjectOutputStream(fileOut)) {

            OrderedList<Integer> orderedList = new OrderedList<>();
            orderedList.add_element(5);
            orderedList.add_element(3);
            orderedList.add_element(7);
            orderedList.add_element(1);

            objOut.writeObject(orderedList);
        } catch (java.io.IOException e) {
            e.printStackTrace();
        }

        try (FileInputStream fileIn = new FileInputStream(filename);
             ObjectInputStream objIn = new ObjectInputStream(fileIn)) {

            OrderedList<Integer> newList = (OrderedList<Integer>) objIn.readObject();
            System.out.println(newList);
        } catch (java.io.IOException | ClassNotFoundException e) {
            e.printStackTrace();
        }
    }
}
