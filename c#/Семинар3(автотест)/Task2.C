using System;
					
public class Program
{
	public static void Main()
	{
		Console.WriteLine("Введите число ");
		double x = double.Parse((Console.ReadLine()));
		double n = 1;
		while (n < x)
		{
			double result = Math.Pow(n,3);
		
		    Console.WriteLine(result);
		
		n++;
		}
		
	}
}