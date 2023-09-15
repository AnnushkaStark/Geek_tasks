using System;

class Program
{
    static void Main()
    {
        // Создание генератора случайных чисел
        Random random = new Random();

        // Размер массива
        int size = 10;

        // Создание массива и заполнение случайными трехзначными числами
        int[] array = new int[size];
        for (int i = 0; i < size; i++)
        {
            array[i] = random.Next(100, 1000);
        }

        // Подсчет количества четных чисел
        int count = 0;
        for (int i = 0; i < size; i++)
        {
            if (array[i] % 2 == 0)
            {
                count++;
            }
        }

        // Вывод результата
        Console.WriteLine($"Количество четных чисел в массиве: {count}");
    }
}