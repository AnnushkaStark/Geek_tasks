using System;
					
public class Program
{
	public static void Main()
	{
		Console.WriteLine("Введите число а: ");
		int a =int.Parse(Console.ReadLine());
		Console.WriteLine("Введите число b: ");
		int b = int.Parse(Console.ReadLine());
		if (a > b)
		{ 
			Console.Write("Большее число : ");
			Console.WriteLine(a);
			Console.Write("Меньшее число : ");
			Console.WriteLine(b);
			
		}
		else if (b > a)
		{
	         Console.Write("Большее число : ");
			 Console.WriteLine(b);
			 Console.Write("Меньшее число : ");
			 Console.WriteLine(a);
		}
		else if (b == a)
		{
	         Console.WriteLine("Числа равны");
			
		}
	}
}