#include <iostream>
using namespace std;

/* Project Euler #5:
 * 2520 is the smallest number that can be divided by each of the numbers
 * from 1 to 10 without any remainder.
 *
 * What is the smallest positive number that is evenly divisible by
 * all of the numbers from 1 to 20? */

/* Note 1:
 * If the number is to be divisible by 20, then it is divisible by the
 * factors of 20 (i.e; 2, 4, 5, 10).
 * Similarly for all non-prime numbers greater than 11.
 *
 * Note 2:
 * Since the number is definitely divisible by 20, it will start at 20 and
 * increment over 20s. */

bool isDivisibleByAll(long number)
{
    for (int x = 11; x <= 20; x++) {
        if (number % x != 0) {
            return false;
        }
    }
    return true;
}
int main()
{
    long number = 20;
    while (true) {
        if (isDivisibleByAll(number)) {
            break;
        } else {
            number += 20;
        }
    }
    // Answer: 232792560
    cout << "Number evenly divisible by all numbers from 1 to 20: "
         << number << endl;
    return 0;
}
