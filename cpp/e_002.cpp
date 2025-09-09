// Answer given by this program is: 4613732

#include <iostream>

int main()
{
    int sum = { 0 };
    int pp_val = { 0 };
    int p_val  = { 1 };
    {
        int i{ 2 };
        while (true)
            {
                i = pp_val + p_val;
                if (i > 4000000)
                    break;
                pp_val = p_val;
                p_val = i;
                std::cout << i << ' '; // i follows the Fibonacci numbers here
                if ((i % 2) == 0)
                    sum += i;
            }
    }
    {
        // std::cout << i << ' ';
        // if ((i %  3) == 0)
        // {
        //     std::cout << i << '\n';
        //     sum += i;
        //     continue;
        // }
        // if ((i % 5) == 0)
        // {
        //     std::cout << i << '\n';
        //     sum += i;
        //     continue;
        // }
    }

    std::cout << "\nFinished, sum is equal to " << sum;

    return 0;
}