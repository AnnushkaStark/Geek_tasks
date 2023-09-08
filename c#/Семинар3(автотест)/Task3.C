using System;
					
public class Program
{
	public static void Main()
	{
		Console.WriteLine("Введите  число   ");
		string s = Console.ReadLine();
        char[] sReverse = s.ToCharArray();
        Array.Reverse(sReverse);
        string s1 = new string(sReverse);
		if(s == s1)
		{
			Console.WriteLine("Это палиндорм");
		
		}
		else
		{
		Console.WriteLine("Это не палиндорм");
		}
	}
}