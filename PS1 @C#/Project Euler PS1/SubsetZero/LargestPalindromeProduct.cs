using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Project_Euler_PS1
{
    class LargestPalindromeProduct
    {
        public LargestPalindromeProduct()
        {
            Console.WriteLine("  A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99. \n  Find the largest palindrome made from the product of two 3-digit numbers.");
            Console.WriteLine();
            double value = 999 * 999;
            bool done = false;
            double temp =0;
            while (!done)
            {
                while (!isPal(value))
                    value--;
                for (int i = 999; i > 99; i--)
                {
                    temp = value / i;
                    if ((temp - Math.Truncate(temp) == 0) && (temp < 1000) && (temp > 99))
                    {
                        done = true;
                        break;
                    }

                }
                Console.WriteLine(value + "  NOPE");
                value--;
            }
            value++;
            Console.WriteLine(value + " = {0} * {1}",temp,  value /temp);
        }

        private bool isPal(double value)
        {
            var cur = value.ToString().ToList();
            var Rev = value.ToString().ToList();
            Rev.Reverse();
            if (Rev.SequenceEqual(cur))
                return true;
            else return false;
        }
    }
}