#include <stdio.h>
#include <stdlib.h>
#include <string.h>

/* Project Euler #4:
 * A palindromic number reads the same both ways.
 * The largest palindrome made from the product of
 * two 2-digit numbers is 9009 = 91 × 99.
 *
 * Find the largest palindrome made from the product of
 * two 3-digit numbers.*/

char* to_str(int);
char* reverse_str(char*);
int is_palin(int);

int main()
{
    int product;
    int max = 0;
    for (int x = 100; x < 1000; x++) {
        for (int y = 100; y < 1000; y++) {
            product = x * y;
            if (is_palin(product) && product > max) {
                max = product;
            }
        }
    }
    // Answer: 906609
    printf("The largest palindrome of two 3-digit numbers multiplied: %d\n", max);
    return 1;
}

// Variation of itoa @ http://www.strudel.org.uk/itoa/
char* to_str(int val) 
{
    static char buf[32] = {0};
    int i = 30;
    int base = 10;
    for (; val && i ; --i, val /= base) {
        buf[i] = "0123456789abcdef"[val % base];
    }
    return &buf[i + 1];
}

char* reverse_str(char *string) 
{
    int len = strlen(string);
    char *reversed = malloc(sizeof(char) * len);
    for (int i = 0; i < len; i++) {
        reversed[i] = string[len - (i + 1)];
    }
    return reversed;
}

int is_palin(int number)
{
    char *str_number = to_str(number);
    char *reversed_number = reverse_str(str_number);
    if (strcmp(str_number, reversed_number) == 0) {
        free(reversed_number);
        return 1;
    }
    free(reversed_number);
    return 0;
}
