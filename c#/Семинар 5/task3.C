using System;

class Program
{
    static void Main()
    {
        // Создание массива вещественных чисел
        double[] array = { 10.5, 7.2, 15.8, 9.1, 12.6 };

        // Нахождение максимального и минимального элементов массива
        double max = array[0];
        double min = array[0];
        for (int i = 1; i < array.Length; i++)
        {
            if (array[i] > max)
            {
                max = array[i];
            }
            if (array[i] < min)
            {
                min = array[i];
            }
        }

        // Вычисление разницы между максимальным и минимальным элементами
        double difference = max - min;

       
        Console.WriteLine($"Разница между максимальным и минимальным элементами: {difference}");
    }
}

	

	
