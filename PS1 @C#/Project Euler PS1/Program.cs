using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Project_Euler_PS1
{
    class Program
    {
        private const int NumberOfProblems = 1;

        static void Main(string[] args)
        {
            menu();
        }

        private static void menu()
        {
           // Console.Clear();
            Console.WriteLine("Project Euler Problem set 1");
            Console.WriteLine("Gerhard Aggenbach :)");
            
            //MENU ITEMS vvv

            DisplayMenuItems();
            int key = int.Parse(Console.ReadLine());
            Console.WriteLine("");
            switch (key)
            {
                #region [ 1 - 10]
                case 1:
                    {
                        MultiplesOf3And5 PE1 = new MultiplesOf3And5();
                        break;
                    }
                case 2:
                    {
                        EvenFibonacci PE1 = new EvenFibonacci();
                        break;
                    }
                case 3:
                    {
                        LargestPrimeFactor PE1 = new LargestPrimeFactor();
                        break;
                    }
                case 4:
                    {
                        LargestPalindromeProduct PE1 = new LargestPalindromeProduct();
                        break;
                    }
                case 5:
                    {
                        SmallestMultiple PE1 = new SmallestMultiple();
                        break;
                    }
                case 6:
                    {
                        SumSquareDiff PE1 = new SumSquareDiff();
                        break;
                    }
                case 7:
                    {
                        BIGstPrime PE1 = new BIGstPrime();
                        break;
                    }
                case 8:
                    {
                        LargestProductInSeries PE1 = new LargestProductInSeries();
                        break;
                    }
                case 9:
                    {
                        SpecialPythagoreanTriplet PE1 = new SpecialPythagoreanTriplet();
                        break;
                    }
                case 10:
                    {
                        SummationPrimes PE1 = new SummationPrimes();
                        break;
                    }
                #endregion

                #region [ 11 - 20]
                case 11:
                    {
                        LargestProductInGrid PE1 = new LargestProductInGrid();
                        break;
                    }
                case 12:
                    {
                        HighlyDivisibleTriangularNumber PE1 = new HighlyDivisibleTriangularNumber();
                        break;
                    }
                case 13:
                    {
                        LargeSum PE1 = new LargeSum();
                        break;
                    }
                case 14:
                    {
                        LongestCollatz PE1 = new LongestCollatz();
                        break;
                    }
                case 15:
                    {
                        LatticePath PE1 = new LatticePath();
                        break;
                    }
                case 16:
                    {
                        PowerDigitSum PE1 = new PowerDigitSum();
                        break;
                    }
                case 17:
                    {
                        NumberLetterCount PE1 = new NumberLetterCount();
                        break;
                    }
                #endregion

                #region [ 21 - 30]
                #endregion

                #region [ 31 - 40]
                #endregion

                #region [ 41 - 50]
                #endregion

                default:
                    {
                        Environment.Exit(0);
                        break;
                    }

            }
            //MENU ITEMS ^^^
            Console.WriteLine("Press any key to continue");
            Console.ReadKey();
            menu();
        }

        private static void DisplayMenuItems()
        {
            Console.WriteLine("1. Multiples of 3 and 5");
            Console.WriteLine("2. Even Fibonacci numbers");
            Console.WriteLine("3. Largest Prime Factor");
            Console.WriteLine("4. Largest Palindrome product");
            Console.WriteLine("5. Samllest Multiple");
            Console.WriteLine("6. Sum square difference");
            Console.WriteLine("7. 10001st prime");
            Console.WriteLine("8. Largest product in a series");
            Console.WriteLine("9. Special Pythagorean triplet");
            Console.WriteLine("10. Summation of Primes");

            Console.WriteLine("11. Largest product in a grid");
            Console.WriteLine("12. Highly divisible triangular number");
            Console.WriteLine("13. Large Sum");
            Console.WriteLine("14. Longest Collatz Number");
            Console.WriteLine("15. Lattice Path");
            Console.WriteLine("16. Power Digit Sum");
            Console.WriteLine("17. Number Letter Counts");
            Console.WriteLine("18. ");
            Console.WriteLine("19. ");
            Console.WriteLine("20. ");
            Console.WriteLine("any unlisted number to exit");
            Console.WriteLine();
        }


    }
}
