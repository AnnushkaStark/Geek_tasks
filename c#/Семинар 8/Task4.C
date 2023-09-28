class Program
{
    static void Main()
    {
        int n = 4;  // Размер массива
        int[,] array = new int[n, n];  // Создание массива

        int value = 1;  // Начальное значение для заполнения
        int rowStart = 0, rowEnd = n - 1;  // Границы строк
        int colStart = 0, colEnd = n - 1;  // Границы столбцов

        // Заполнение массива спирально
        while (value <= n * n)
        {
            // Заполнение верхней строки
            for (int i = colStart; i <= colEnd; i++)
            {
                array[rowStart, i] = value++;
            }
            rowStart++;

            // Заполнение правого столбца
            for (int i = rowStart; i <= rowEnd; i++)
            {
                array[i, colEnd] = value++;
            }
            colEnd--;

            // Заполнение нижней строки
            for (int i = colEnd; i >= colStart; i--)
            {
                array[rowEnd, i] = value++;
            }
            rowEnd--;

            // Заполнение левого столбца
            for (int i = rowEnd; i >= rowStart; i--)
            {
                array[i, colStart] = value++;
            }
            colStart++;
        }

        // Вывод массива
        for (int i = 0; i < n; i++)
        {
            for (int j = 0; j < n; j++)
            {
                Console.Write(array[i, j] + "\t");
            }
            Console.WriteLine();
        }
    }
}