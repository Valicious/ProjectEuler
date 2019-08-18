using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Project_Euler_PS1
{
    class LongestCollatz
    {
        public LongestCollatz()
        {
            Console.WriteLine();
            int chainSize = 0;
            for (int i = 100000; i < 1000000; i++)
            {
                int size = GetChainSize(i);
                if (size > chainSize)
                {
                    chainSize = size;
                    Console.WriteLine(i + ": " + size);
                }
            }
        }

        private int GetChainSize(long cur)
        {
            long temp = cur;
            int count = 0;
            while (cur != 1)
            {
                count++;
                if (cur % 2 == 0)
                    cur = cur / 2;
                else cur = (3 * cur) + 1;
            }
            return count;
        }
    }
}
