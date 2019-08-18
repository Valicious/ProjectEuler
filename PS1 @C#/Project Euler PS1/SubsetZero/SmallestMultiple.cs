using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Project_Euler_PS1
{
    class SmallestMultiple
    {
        public SmallestMultiple()
        {
            Console.WriteLine("  2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder. \n  What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?");
            Console.WriteLine();
            for (int i = 10 * 9; i < (int.MaxValue); i += 10)
            {
                if (i % 9 == 0)
                    if (i % 8 == 0)
                        if (i % 7 == 0)
                            if (i % 6 == 0)
                            {
                                Console.WriteLine(i);
                                break;
                            }
            }
            for (int i = 20 * 19; i < (int.MaxValue); i += 20)
            {
                if (i % 19 == 0)
                    if (i % 18 == 0)
                        if (i % 17 == 0)
                            if (i % 16 == 0)
                                if (i % 15 == 0)
                                    if (i % 14 == 0)
                                        if (i % 13 == 0)
                                            if (i % 12 == 0)
                                                if (i % 11 == 0)
                                                {
                                                    Console.WriteLine(i);
                                                    break;
                                                }
            }
        }
    }
}