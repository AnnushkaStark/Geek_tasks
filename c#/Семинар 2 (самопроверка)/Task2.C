using System;
using System.Collections.Generic;
using System.Linq;
using System.Text.RegularExpressions;

namespace HelloWorld
{
	public class Program
	{
		public static void Main(string[] args)
		{
			Console.WriteLine("Ведите трехзначное число  ");
			  int n = int.Parse(Console.ReadLine());
			  if (n < 100 )
			{
			  Console.WriteLine("Нет третьего числа");
			
			}
			  else if (n >= 1000 && n < 10000)
			  {
			    int a = n % 100;
			    int b = a / 10;
			    Console.WriteLine(b);
			  }
			  else if (n > 99 && n < 1000)
			  {
			    int c = n % 10 ;
			    Console.WriteLine(c);
			  }
			  else{
			     Console.WriteLine("Слишком большое число");
			}
		}
	}
}