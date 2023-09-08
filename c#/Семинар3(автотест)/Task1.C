using System;
					
public class Program
{
	public static void Main()
	{
		Console.WriteLine("Введите точку х1  ");
		double x1 = double.Parse((Console.ReadLine()));
		Console.WriteLine("Введите точку y1  ");
		double y1 = double.Parse((Console.ReadLine()));
		Console.WriteLine("Введите точку z1  ");
		double z1 = double.Parse((Console.ReadLine()));
		Console.WriteLine("Введите точку х2  ");
		double x2 = double.Parse((Console.ReadLine()));
		Console.WriteLine("Введите точку y2  ");
		double y2 = double.Parse((Console.ReadLine()));
		Console.WriteLine("Введите точку z2  ");
		double z2 = double.Parse((Console.ReadLine()));
		double result = Math.Sqrt((x2 - x1)*(x2 - x1) + (y2 - y1)* (y2 - y1)+ (z2 - z1)*(z2 - z1));
		Console.Write("Расстояние в 3D пространстве между точками =");
		Console.WriteLine(result);
		
	}
}