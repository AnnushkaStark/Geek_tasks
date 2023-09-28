using System;

class Program
{
    static void Main()
    {
        int[,] array = new int[,]
        {
            {5, 3, 8, 2},
            {9, 1, 7, 4},
            {6, 2, 0, 3}
        };

        int rows = array.GetLength(0);
        int cols = array.GetLength(1);

        int minSumRow = 0;  // Индекс строки с наименьшей суммой элементов
        int minSum = int.MaxValue;  // Начальное значение для сравнения

        // Находим строку с наименьшей суммой элементов
        for (int row = 0; row < rows; row++)
        {
            int sum = 0;  // Переменная для хранения суммы элементов в текущей строке

            // Считаем сумму элементов текущей строки
            for (int col = 0; col < cols; col++)
            {
                sum += array[row, col];
            }

            // Если сумма элементов текущей строки меньше предыдущего наименьшего значения,
            // обновляем значения индекса и наименьшей суммы
            if (sum < minSum)
            {
                minSum = sum;
                minSumRow = row;
            }
        }

        Console.WriteLine("Строка с наименьшей суммой элементов: ");

        // Выводим строку с наименьшей суммой элементов
        for (int col = 0; col < cols; col++)
        {
            Console.Write(array[minSumRow, col] + " ");
        }

        Console.WriteLine();
    }
}
