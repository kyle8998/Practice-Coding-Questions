#include <stdio.h>
#include <stdbool.h>

//-----------------------------------------------------------------------------

bool isPalindrome(int x){

    int temp = x, digits = 1;
    // If x is negative
    if (x < 0)
        return false;

    // Finds  1^digits
    while (temp >= 10){
        temp /= 10;
        digits *= 10;
    }

    while (x){
        if ((x % 10) != (x / digits))
            return false;
        // Removes a digit off each side
        x = (x % digits) / 10;
        // Removes 2 digits
        digits /= 100;
    }
    // If it makes it this far it is a palindrome
    return true;
}

//-----------------------------------------------------------------------------
// Testing

int main(){
    int test = 1000021;
    printf("%d\n", isPalindrome(test));
    return 0;
}

