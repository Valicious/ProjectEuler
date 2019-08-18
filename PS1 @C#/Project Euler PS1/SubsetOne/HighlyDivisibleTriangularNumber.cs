using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Project_Euler_PS1
{
    class HighlyDivisibleTriangularNumber
    {
        public HighlyDivisibleTriangularNumber()
        {
            Console.WriteLine();
            long triNum = 0;
            int max = int.MinValue;
            for (int i = 1; true; i++)
            {
                triNum += i;
                int temp = getDivCount(triNum);
                if (temp > max)
                {
                    Console.WriteLine(triNum + ": " + temp);
                    max = temp;
                }
                if (temp > 500)
                    break;

            }
        }

        private int getDivCount(long input)
        {
            int count = 1;
            if (input % 20 != 0) return 0;
            for (long i = (long)Math.Ceiling(input / 2.0); i > 0; i--)
            {
                if (input % i == 0)
                    count++;
            }
            ; return count;
        }
    }
}
