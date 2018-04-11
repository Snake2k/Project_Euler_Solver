#include <iostream>
#include <string>
using namespace std;

/* Project Euler #4:
 * A palindromic number reads the same both ways.
 * The largest palindrome made from the product of two 2-digit numbers is
 * 9009 = 91 × 99.
 * Find the largest palindrome made from the product of two 3-digit numbers. */

bool isPalin(string number)
{
    string mirror = "";
    for (int i = number.length()-1; i >= 0; i--) {
        mirror += number[i];
    }
    if (number == mirror) {
        return true;
    } else {
        return false;
    }
}

int main()
{
    long number;
    long largestPalin = 0;
    for (int x = 100; x < 999; x++) {
        for (int y = 100; y < 999; y++) {
            number = x * y;
            if(isPalin(to_string(number)) && number > largestPalin) {
                largestPalin = number;
            }
        }
    }
    // Answer: 906609
    cout << "The largest palindrome made from" <<
            "the product of two 3-digit numbers: " <<
            largestPalin << endl;
    return 0;
}
