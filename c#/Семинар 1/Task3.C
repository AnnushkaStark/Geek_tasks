using System;
					
public class Program
{
	public static void Main()
	{
		Console.WriteLine("Введите число а: ");
		int a =int.Parse(Console.ReadLine());
		if (a % 2 == 0)
		{ 
			Console.Write("Это число четное ");
			Console.WriteLine(a);
			
		}
		else if (a % 2 != 0)
		{
	         Console.Write("Это число не четное");
			 
		
		}
		
		
	}
}