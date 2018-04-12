#include <iostream>
#include <cmath>
using namespace std;

/* Project Euler #7:
 * By listing the first six prime numbers:
 * 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
 *
 * What is the 10 001st prime number? */

bool isPrime(int number)
{
    while (number % 2 == 0) {
        number /= 2;
    }
    for (int x = 2; x < number; x++) {
        if (number % x == 0) {
            return false;
        }
    }
    return true;
}

int main()
{
    int count = 0;
    int number = 2;
    while (count < 10001) {
        if (isPrime(number)) {
            count++;
        }
        number++;
    }
    // Answer: 104743
    cout << "The 10,001st prime: "
         << number - 1 << endl;
    return 0;
}
