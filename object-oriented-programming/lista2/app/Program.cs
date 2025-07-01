// Dawid Pawliczek, lista 2 zadanie 1

using System;

class IntStream
{
    public virtual int next() { return 0; }
    public virtual bool eos() { return false; }
    public virtual void reset() { }
}

class FibStream : IntStream
{
    private int a = 1;
    private int b = 1;

    public override int next()
    {
        int nextValue = a;
        int c = a + b;
        a = b;
        b = c;
        return nextValue;
    }

    public override bool eos()
    {
        return false;
    }

    public override void reset()
    {
        a = 0;
        b = 1;
    }
}

class RandomStream : IntStream
{
    private Random random = new Random();

    public override int next()
    {
        return random.Next();
    }

    public override bool eos()
    {
        return false;
    }

    public override void reset()
    {
        random = new Random();
    }
}

class RandomWordStream
{
    private RandomStream random = new RandomStream();
    private FibStream fibo = new FibStream();
    private string chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz";

    public string next()
    {
        string returnedString = "";
        int fiboNum = fibo.next();        

        for (int i = 1; i <= fiboNum; i++)
        {
            int randomNum = random.next();
            returnedString += chars[randomNum % chars.Length];

        }
        return returnedString;
    }

    public bool eos()
    {
        return false;
    }

    public void reset()
    {
        random = new RandomStream();
        fibo = new FibStream();
    }
}

class Program
{
    static void Main()
    {
        RandomWordStream rws = new RandomWordStream();
        for (int i = 0; i < 10; i++)
        {
            Console.WriteLine(rws.next());
        }
    }
}