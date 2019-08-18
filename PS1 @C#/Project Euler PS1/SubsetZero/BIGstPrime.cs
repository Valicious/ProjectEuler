using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Project_Euler_PS1
{
    class BIGstPrime
    {
        public BIGstPrime()
        {
            Console.WriteLine("By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.  \nWhat is the 10 001st prime number?");
            Console.WriteLine();
            int count = 6;
            for (long i = 17; i < long.MaxValue; i++)
            {
                if (IsPrime(i))
                {
                    count++;
                    if (count == 10001)
                    {
                        Console.WriteLine(i);
                        break;
                    }
                    else Console.WriteLine(count + ". Nope : " + i);
                }
            }
        }

        private bool IsPrime(long input)
        {
            for (long test = 2; test < input; test++)
                if (input % test == 0)
                    return false;
            return true;
        }
    }
}