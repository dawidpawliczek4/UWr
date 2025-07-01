// Dawid Pawliczek lista 3 zadanie 1

// nullable disabled

//dotnet new classlib List
//mv l3z1.cs List
//cd l3z1
//dotnet add reference List(pelna sciezka)
//dotnet build

using System;

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

public class Lista<T>
{
    public Node<T> head;
    public Node<T> tail;

    public Lista()
    {
        head = null;
        tail = null;
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
            node.Next = head;
            head.Prev = node;
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
}
