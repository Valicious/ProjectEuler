using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Project_Euler_PS1
{
    class SpecialPythagoreanTriplet
    {
        public SpecialPythagoreanTriplet()
        {
            //a^2 + b^2 = c^2
            //where a + b + c = 1000
            // a < b < c

            Console.WriteLine();
            double c = 1;
            bool exit = false;
            for (int b = 1; !exit; b++)
                for (int a = 1; a < b; a++)
                {
                    c = Math.Sqrt(Math.Pow(a, 2) + Math.Pow(b, 2));
                    if (c - Math.Truncate(c) == 0)
                    {
                        Console.WriteLine("{0}^2 + {1}^2 = {2}^2 = {3} \t\t {4}", a, b, c, Math.Pow(c, 2), a + b + c);
                        if (a + b + c == 1000)
                        {
                            Console.WriteLine(a*b*c);
                            exit = true;
                            break;
                        }
                    }
                }
        }
    }
}