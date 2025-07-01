class Program
{
    static void Main()
    {
        Lista<int> lista = new Lista<int>();
        lista.push_front(1);
        lista.push_front(2);
        lista.push_back(3);
        lista.push_back(4);
        Console.WriteLine(lista.pop_front());
        Console.WriteLine(lista.pop_back());
        Console.WriteLine(lista.pop_front());
        Console.WriteLine(lista.pop_back());        
    }
}