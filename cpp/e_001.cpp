// Answer given by this program is: 233168

#include <iostream>

int main()
{
    int sum = { 0 };
    for (int i{ 1 }; i < 1000; ++i)
    {
        if ((i %  3) == 0)
        {
            // std::cout << i << '\n';
            sum += i;
            continue;
        }
        if ((i % 5) == 0)
        {
            // std::cout << i << '\n';
            sum += i;
            continue;
        }
    }

    std::cout << "Finished, sum is equal to " << sum;

    return 0;
}