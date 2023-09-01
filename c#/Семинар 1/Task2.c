using System;
					
public class Program
{
	public static void Main()
	{
		Console.WriteLine("Введите число а: ");
		int a =int.Parse(Console.ReadLine());
		Console.WriteLine("Введите число b: ");
		int b = int.Parse(Console.ReadLine());
		Console.WriteLine("Введите число c: ");
		int c = int.Parse(Console.ReadLine());
		if (a > b && a > c)
		{ 
			Console.Write(" Самое большее число : ");
			Console.WriteLine(a);
			
		}
		else if (b > a && b > c )
		{
	         Console.Write("Самое большее число : ");
			 Console.WriteLine(b);
		
		}
		else if (c > a && c > b )
		{
	        Console.Write("Самое большее число : ");
			Console.WriteLine(c);
			
		}
		else if (c == a  && c == b)
		{
			Console.Write("Ваши числа равны ");
		}
	}
}