#include <iostream>
#include <cmath>
using namespace std;

/* Project Euler #3:
 * The prime factors of 13195 are 5, 7, 13 and 29.
 *
 * What is the largest prime factor of the number 600851475143 ? */

bool isPrime(long number)
{
    while (number % 2 == 0) {
        number /= 2;
    }
    for (long i = 3; i < number; i++) {
        if (number % i == 0) {
            return false;
        }
    }
    return true;
}

int main()
{
    long largestprime = 0;
    const long limit = 600851475143;
    for (long x = 2; x <= sqrt(limit); x++) {
        if ((limit % x == 0) &&
            isPrime(x)       &&
            x > largestprime) {
            largestprime = x;
        }
    }
    // Answer: 6857
    cout << "The largest prime factor of 600851475143: "
         << largestprime << endl;
    return 0;
}
