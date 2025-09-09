// Answer given by this program is: 
// The prime factors of 13195 are 5, 7, 13 and 29
// What is the largest prime factor of the number 600851475143

#include <iostream>
#include <cmath>
#include <cstdint>
#include <list>

bool is_integer(double k)
{
    return std::floor(k) == k;
}

bool is_prime(int k, std::list<double> prime_list)
{
    for (int prime : prime_list)
    {
        std::cout << prime << std::endl;
        if ((k % prime) == 0)
        {
            // std::cout << k << " is not prime." << std::endl;
            return false;
        }
    }
    return true;
}

int main()
{
    double value = { 600851475143 };
    double largest_prime = { 0 };
    std::list<double> prime_list = { 2 };
    for (float i = { 3 }; i <= (std::sqrt(value)); i++)
    {
        if (is_prime(i, prime_list))
        {
            std::cout << i << " is prime." << std::endl;
            prime_list.push_back(i);
            double division_result = { 0 };
            division_result = value / i;
            if (is_integer(division_result))
            {
                std::cout << i << " is a prime factor of " << value << std::endl;
                largest_prime = i;
            }
        }

    }
    std::cout << "\nFinished, largest prime factor is " << largest_prime;

    return 0;
}