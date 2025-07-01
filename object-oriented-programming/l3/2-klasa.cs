// Dawid Pawliczek lista 3 zad 2

//dotnet new classlib Dict
//mv l3z2.cs Dict
//cd l3z2
//dotnet add reference Dict(pelna sciezka)
//dotnet build

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
