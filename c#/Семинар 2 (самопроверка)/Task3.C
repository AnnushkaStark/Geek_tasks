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
			Console.WriteLine("Ведите  число от одного до семи ");
			  int n = int.Parse(Console.ReadLine());
			  if (n == 6 )
			{
			  Console.WriteLine("Это суббота выходной день");
			
			}
			  else if (n ==7 )
			{
			    
			 Console.WriteLine("Это воскресенье выходной день");
			}
			  else if (n == 5)
			{
			  Console.WriteLine("Это пятница  рабочий  день");
			}
			  else if (n == 4)
			{
			  Console.WriteLine("Это четверг рабочий  день");
			}
		     else if (n == 3)
			{
			   Console.WriteLine("Это среда  рабочий  день");
			}
			   else if (n == 2)
			{
			   Console.WriteLine("Это вторник  рабочий  день");
			}
			   else if (n == 1)
			{
			   Console.WriteLine("Это понедельник рабочий  день");
			}
			  else if (n <= 0)
			{
			     Console.WriteLine("Неверный ввод данных");
			}
			   else if (n > 7)
			{
			   Console.WriteLine("Неверный ввод данных");
			}
		}
	  
	}
}