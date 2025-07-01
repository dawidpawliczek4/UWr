// Dawid Pawliczek, lista 4 zadanie 1

using System;
using System.Collections;
using System.Collections.Generic;

interface ListCollection<T>
{
    bool is_empty();
}

public class Node<T>
{
    public T Data;
    public Node<T> Next;
    public Node<T> Prev;

    public Node(T data)
    {
        Data = data;
        Next = null;
        Prev = null;
    }
}

public class ListEnum<T> : IEnumerator<T>
{
    private Lista<T> list;
    private Node<T> current;
    private bool isFirst;

    public ListEnum(Lista<T> list)
    {
        this.list = list;
        current = null;
        this.isFirst = true;
    }

    public T Current
    {
        get
        {
            if (current == null)
            {
                throw new InvalidOperationException();
            }
            return current.Data;
        }
    }

    object IEnumerator.Current
    {
        get
        {
            return Current;
        }
    }

    public void Dispose()
    {
    }

    public bool MoveNext()
    {
        if (isFirst) {
            current = list.head;
            isFirst = false;
        }
        else if (current != null)
        {
            current = current.Next;
        }
        return current != null;
    }

    public void Reset()
    {
        current = list.head;
    }


}

public class Lista<T> : IEnumerable<T>
{
    public Node<T> head;
    public Node<T> tail;

    public int length
    {
        get
        {
            int l = 0;
            foreach (T e in this)
            {
                l++;
            }
            return l;
        }
    }

    public T this[int index] {
        get {            
            if (index < 0 || index > this.length) {
                throw new IndexOutOfRangeException("Index was outside the bounds of the list.");
            }
            Node<T> current = head;
            for (int i = 0; i < index; i++)
            {                
                current = current.Next;
            }
            return current.Data;
        }
    }

    public Lista()
    {
        head = null;
        tail = null;
    }

    public IEnumerator<T> GetEnumerator()
    {
        return new ListEnum<T>(this);
    }

    IEnumerator IEnumerable.GetEnumerator()
    {
        return GetEnumerator();
    }

    public void push_front(T elem)
    {
        Node<T> node = new Node<T>(elem);
        if (this.is_empty())
        {
            head = tail = node;
        }
        else
        {
            head.Prev = node;
            node.Next = head;
            head = node;
        }
    }

    public void push_back(T elem)
    {
        Node<T> node = new Node<T>(elem);
        if (this.is_empty())
        {
            head = tail = node;
        }
        else
        {
            tail.Next = node;
            node.Prev = tail;
            tail = node;
        }
    }

    public T pop_front()
    {
        if (this.is_empty())
        {
            throw new InvalidOperationException("Cannot pop from an empty list.");
        }

        T value = head.Data;
        if (head == tail)
        {
            head = tail = null;
        }
        else
        {
            head = head.Next;
            head.Prev = null;
        }

        return value;
    }

    public T pop_back()
    {
        if (this.is_empty())
        {
            throw new InvalidOperationException("Cannot pop from an empty list.");
        }

        T value = tail.Data;
        if (head == tail)
        {
            head = tail = null;
        }
        else
        {
            tail = tail.Prev;
            tail.Next = null;
        }

        return value;
    }

    public bool is_empty()
    {
        return head == null;
    }

    public override string ToString()
    {
        string result = "";
        Node<T> current = head;
        while (current != null)
        {
            result += current.Data + " ";
            current = current.Next;
        }
        return result;
    }
}


public class MyDictionary<K, V> : ListCollection<K>
{
    private List<K> keys;
    private List<V> values;

    public MyDictionary()
    {
        keys = new List<K>();
        values = new List<V>();
    }

    public void Add(K key, V value)
    {
        if (!keys.Contains(key))
        {
            keys.Add(key);
            values.Add(value);
        }
        else
        {
            throw new ArgumentException("An element with the same key already exists in the dictionary.");
        }
    }

    public V Get(K key)
    {
        int index = keys.IndexOf(key);
        if (index == -1)
        {
            throw new KeyNotFoundException("The given key was not present in the dictionary.");
        }
        return values[index];
    }

    public bool Remove(K key)
    {
        int index = keys.IndexOf(key);
        if (index != -1)
        {
            keys.RemoveAt(index);
            values.RemoveAt(index);
            return true;
        }
        return false;
    }

    public int Count => keys.Count;

    public bool is_empty()
    {
        return keys.Count == 0;
    }

}

class Program
{
    public static void Main()
    {
        Lista<int> list = new Lista<int>();
        list.push_back(1);
        list.push_back(2);
        list.push_back(3);
        list.push_back(17);
        list.push_front(0);

        Console.WriteLine(list[0]);

        foreach (int e in list)
        {
            Console.WriteLine(e);
        }
                
    }
}