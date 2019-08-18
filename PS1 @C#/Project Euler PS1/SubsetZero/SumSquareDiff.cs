using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Project_Euler_PS1
{
    internal class SumSquareDiff
    {
        public SumSquareDiff()
        {
            Console.WriteLine("  The sum of the squares of the first ten natural numbers is, \n 12 + 22 + ... + 102 = 385 \n  The square of the sum of the first ten natural numbers is, \n (1 + 2 + ... + 10)2 = 552 = 3025 \n  Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640. \n  Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.");
            Console.WriteLine();

            double sumSquare = 0;
            double sum = 0;
            for (int i = 1; i <= 100; i++)
            {
                sumSquare += Math.Pow(i, 2);
                sum += i;
            }
            sum = Math.Pow(sum, 2);
            Console.WriteLine(sum - sumSquare);
        }
    }
}