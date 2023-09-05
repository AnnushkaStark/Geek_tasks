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
			  if (n < 100 && n < 999 )
			{
			  Console.WriteLine("Число не трехзначное");
			
			}
			  else{
			    int a = n % 100;
			    int b = a / 10;
			    Console.WriteLine(b);
			
			}
		}
	}
}