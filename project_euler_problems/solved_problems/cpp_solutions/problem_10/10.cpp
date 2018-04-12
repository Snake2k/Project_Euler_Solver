#include <iostream>
using namespace std;

/* Project Euler #10:
 * The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
 *
 * Find the sum of all the primes below two million. */

void markIndex(bool sieve[], int num, const int size) {
    for (int i = (num * 2); i < size; i += num) {
        sieve[i] = false;
    }
}

int main()
{
    const int SIZE = 2000000;
    bool sieve[SIZE];
    for (int i = 0; i < SIZE; i++) {
        sieve[i] = true;
    }
    for (int i = 2; i < SIZE; i++) {
        if(sieve[i]) {
            markIndex(sieve, i, SIZE);
        }
    }
    long sum = 0;
    for (int i = 2; i < SIZE; i++) {
        if (sieve[i]) {
            sum += i;
        }
    }
    // Answer: 142913828922
    cout << "Sum of all primes < 2 million: "
         << sum << endl;
    return 0;
}
