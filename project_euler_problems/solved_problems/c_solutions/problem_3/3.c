#include <stdio.h>

/* Project Euler #3:
 * The prime factors of 13195 are 5, 7, 13 and 29.
 *
 * What is the largest prime factor of the number 600851475143?
 */

int main()
{
    long number = 600851475143;
    long largest_prime_factor = 1;
    long divisor = 2;
    while (number > 1) {
        if (number % divisor == 0) {
            largest_prime_factor = divisor;
            number = number / divisor;
            while (number % divisor == 0) {
                number = number / divisor;
            }
        }
        divisor++;
    }
    // Answer: 6857
    printf("The largest prime factor: %ld\n", largest_prime_factor);
    return 0;
}
