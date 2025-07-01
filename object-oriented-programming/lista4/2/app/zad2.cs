// Dawid Pawliczek, lista 4 zadanie 2

using System;
using System.Collections;
using System.Collections.Generic;

public class SlowaFibbonacciego : IEnumerable<string>
{
    private List<string> words;

    public SlowaFibbonacciego(int count)
    {
        words = new List<string> { "b", "a" }; // Initialize with the first two words

        while (words.Count < count)
        {
            // Concatenate the last two words to form the new word
            string newWord = words[words.Count - 1] + words[words.Count - 2];
            words.Add(newWord);
        }
    }

    public IEnumerator<string> GetEnumerator()
    {
        for (int i = 0; i < words.Count; i++)
        {
            yield return words[i];
        }
    }

    IEnumerator IEnumerable.GetEnumerator()
    {
        return GetEnumerator();
    }
}

class Program
{
    static void Main()
    {
        SlowaFibbonacciego sf = new SlowaFibbonacciego(6);
        foreach (string s1 in sf)
            foreach (string s2 in sf)
                Console.WriteLine(s1, s2);

        Console.WriteLine("Done");

    }
}