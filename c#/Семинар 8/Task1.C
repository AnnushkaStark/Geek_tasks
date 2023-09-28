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

        // Применяем сортировку по убыванию для каждой строки
        for (int row = 0; row < rows; row++)
        {
            for (int col = 0; col < cols - 1; col++)
            {
                for (int j = col + 1; j < cols; j++)
                {
                    if (array[row, j] > array[row, col])
                    {
                        int temp = array[row, col];
                        array[row, col] = array[row, j];
                        array[row, j] = temp;
                    }
                }
            }
        }
        for (int row = 0; row < rows; row++)
        {
            for (int col = 0; col < cols; col++)
            {
                Console.Write(array[row, col] + " ");
            }
            Console.WriteLine();
        }
    }
}