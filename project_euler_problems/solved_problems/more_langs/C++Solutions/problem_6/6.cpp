#include <iostream>
using namespace std;

/* Project Euler #6:
 * The sum of the squares of the first ten natural numbers is,
 *
 * 1^2 + 2^2 + ... + 10^2 = 385
 * The square of the sum of the first ten natural numbers is,
 *
 * (1 + 2 + ... + 10)^2 = 55^2 = 3025
 * Hence the difference between the sum of the squares of the first
 * ten natural numbers and the square of the sum is 3025 − 385 = 2640.
 *
 * Find the difference between the sum of the squares of the first
 * one hundred natural numbers and the square of the sum. */

int main()
{
    int sum_of_squares = 0;
    int square_of_sums = 0;
    for (int x = 0; x <= 100; x++) {
        sum_of_squares += x*x;
        square_of_sums += x;
    }
    square_of_sums *= square_of_sums;
    // Answer: 25164150
    cout << "Diff between sum of squares and square of sums: "
         << square_of_sums - sum_of_squares << endl;
    return 0;
}
