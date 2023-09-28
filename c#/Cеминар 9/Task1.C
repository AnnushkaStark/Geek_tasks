using System;

class Program
{
    static void Main(string[] args)
    {
        Console.Write("Введите значение N: ");
        int n = int.Parse(Console.ReadLine());

        PrintNumbers(n);

        Console.ReadKey();
    }

    static void PrintNumbers(int n)
    {
        if (n >= 1)
        {
            Console.WriteLine(n);
            PrintNumbers(n - 1);
        }
    }
}
