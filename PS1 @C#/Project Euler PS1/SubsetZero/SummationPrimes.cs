using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Project_Euler_PS1
{
    class SummationPrimes
    {
        public SummationPrimes()
        {
            List<int> value = Enumerable.Range(2, 2000000).ToArray().ToList();
            for (int i = 0; i < Math.Sqrt(2000000); i++)
            {
                if (value[i] != 0)
                    for (int j = value[i] + i; j < value.Count; j += value[i])
                        value[j] = 0;
            }
            value.RemoveAll(a => a == 0);
            var values = value.ConvertAll(x => (long)x);
            Console.WriteLine(values.Sum());
        }
        
        public static long change(int input)
        {
            return (long)input;
        }
    }
}