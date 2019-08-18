using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Project_Euler_PS1
{
    class LatticePath
    {
        public LatticePath()
        {
            Console.WriteLine();
            int x = 20;

            long paths = factorialTop(x+1,x*2) *2;
            paths /= factorial(x-1);
            Console.WriteLine(loop(20,20));
        }

        private long factorialTop(int from, int to)
        {
            long result = 1;
            for (int i = from; i <= to; i++)
                result *= i;
            return result;
        }

        private long factorial(long x)
        {
            if (x == 0) return 1;
            return factorial(x - 1) * x;
        }

        private long loop(int m, int n)
        {
            if ((m == 0) || (n == 0)) return 1;
            return loop(m,n-1) + loop(m-1,n);
        } 
    }
}
