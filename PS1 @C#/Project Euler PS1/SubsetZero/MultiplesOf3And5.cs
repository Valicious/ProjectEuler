using System;

namespace Project_Euler_PS1
{
    class MultiplesOf3And5
    { 

        public MultiplesOf3And5()
        {
            Console.WriteLine("If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9.The sum of these multiples is 23.Find the sum of all the multiples of 3 or 5 below 1000.");
            int sum = 0;
            for (int i = 0; i < 10; i++)
            {
                if (i % 3 == 0)
                    sum += i;
                else if (i % 5 == 0)
                    sum += i;
            }
            Console.WriteLine();
            Console.WriteLine(sum);
            sum = 0;
            for (int i = 0; i < 1000; i++)
            {
                if (i % 3 == 0)
                    sum += i;
                else if (i % 5 == 0)
                    sum += i;
            }
            Console.WriteLine(sum);
        }
    }
}