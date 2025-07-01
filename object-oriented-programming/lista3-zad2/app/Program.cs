using System;
using System.Collections.Generic;

public class MyDictionary<K, V>
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
}



class Program
{
    static void Main()
    {
        MyDictionary<string, int> dict = new MyDictionary<string, int>();
        dict.Add("one", 1);
        dict.Add("two", 2);
        dict.Add("three", 3);
        dict.Add("four", 4);
        dict.Add("five", 5);

        Console.WriteLine(dict.Get("one"));
        Console.WriteLine(dict.Get("two"));
        Console.WriteLine(dict.Get("three"));
        Console.WriteLine(dict.Get("four"));
        Console.WriteLine(dict.Get("five"));

        Console.WriteLine(dict.Remove("three"));
        Console.WriteLine(dict.Remove("three"));

        Console.WriteLine(dict.Count);
    }
}