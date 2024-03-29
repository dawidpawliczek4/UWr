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