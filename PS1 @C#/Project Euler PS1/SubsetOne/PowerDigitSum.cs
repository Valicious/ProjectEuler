using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Project_Euler_PS1
{
    class PowerDigitSum
    {
        public PowerDigitSum()
        {
            //char[] outp = Math.Pow(2, 1000).ToString().ToCharArray();
            //foreach(char c in outp)
            //Console.Write(c);

            int[] worker = new int[] { 2 };
            for (int i = 2; i <= 1000; i++)
                multiply(ref worker, 2);

            //BigInteger ou = 2;
            //for (int i = 2; i < 1000; i++)
            //    ou *= 2;
            int sum = 0;
            for (int i = 0; i < worker.Length; i++)
                sum += worker[i];
            Console.WriteLine(sum.ToString());
        }

        private void multiply(ref int[] worker, int val)
        {
            int ten = 0;
            int mul = 0;
            for (int i = worker.Length - 1; i >= 0; i--)
            {
                mul = (worker[i] * val) + ten;
                if (mul > 9)
                {
                    ten = 1;
                    mul -= 10;
                }
                else ten = 0;
                worker[i] = mul;
            }
            if (ten == 1)
            {
                int[] worker2 = new int[worker.Length + 1];
                worker.CopyTo(worker2,1);
                worker2[0] = 1;
                worker = worker2;
            }
        }
    }
}
