// Dawid Pawliczek, lista 2 zadanie 3

using System;
using System.Text;

public class BigNum
{
    private int[] digits;
    public static int MAX_SIZE = 100;

    public BigNum(int number)
    {
        digits = new int[MAX_SIZE];
        int i = 0;
        while (number > 0 && i < MAX_SIZE)
        {
            digits[i++] = number % 10;
            number /= 10;
        }
    }

    public BigNum Add(BigNum other)
    {
        BigNum result = new BigNum(0);
        int carry = 0;
        for (int i = 0; i < MAX_SIZE; i++)
        {
            int sum = this.digits[i] + other.digits[i] + carry;
            result.digits[i] = sum % 10;
            carry = sum / 10;
        }
        return result;
    }

    public BigNum Subtract(BigNum other)
    {

        for (int i = MAX_SIZE - 1; i >= 0; i--)
        {
            if (this.digits[i] < other.digits[i])
            {
                throw new InvalidOperationException("Nie można odjąć większej liczby od mniejszej.");
            }
            if (this.digits[i] > other.digits[i])
            {
                break;
            }
        }

        BigNum result = new BigNum(0);
        int borrow = 0;
        for (int i = 0; i < MAX_SIZE; i++)
        {
            int sub = this.digits[i] - other.digits[i] - borrow;
            if (sub < 0)
            {
                sub += 10;
                borrow = 1;
            }
            else
            {
                borrow = 0;
            }
            result.digits[i] = sub;
        }
        return result;
    }

    public override string ToString()
    {
        StringBuilder sb = new StringBuilder();
        bool leadingZero = true;
        for (int i = MAX_SIZE - 1; i >= 0; i--)
        {
            if (digits[i] != 0) leadingZero = false;
            if (!leadingZero) sb.Append(digits[i]);
        }
        return sb.Length > 0 ? sb.ToString() : "0";
    }
}

class Program
{
    static void Main()
    {
        BigNum num1 = new BigNum(123);
        BigNum num2 = new BigNum(22);

        BigNum sum = num1.Add(num2);
        BigNum difference = num1.Subtract(num2);

        Console.WriteLine($"Suma: {sum}");
        Console.WriteLine($"Różnica: {difference}");
    }
}