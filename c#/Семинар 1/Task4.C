using System;
					
public class Program
{
	public static void Main()
	{
		Console.WriteLine("Введите число а: ");
		int a =int.Parse(Console.ReadLine());
		int b = 1;
		while (b < a)
		{  
			if ( b % 2 == 0)
			{
			Console.WriteLine(b);
			}
		b ++;
		}
		
	}
}