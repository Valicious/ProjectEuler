using System;

namespace Project_Euler_PS1
{
    class LargestPrimeFactor
    {
        public LargestPrimeFactor()
        {
            Console.WriteLine("The prime factors of 13195 are 5, 7, 13 and 29. \n What is the largest prime factor of the number 600851475143 ?");
            Console.WriteLine();
            long value = 600851475143;
            long prime = 1;
            for (long i = 2; i <= value; i++)
                if (value % i == 0)
                {
                    if (value / i == 1)
                    {
                        if (value == i)
                            prime = i;
                        break;
                    }
                    value = value / i;
                    prime = i;
                    Console.WriteLine(prime);
                }
            Console.WriteLine(prime);
        }
    }
}