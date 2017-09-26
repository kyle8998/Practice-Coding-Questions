#include <stdio.h>
#include <string.h>

int climbStairs(int n) {
    // Dynamic Programming Fibonacci
    int a = 1, b = 1;
    while (n--)
        // a becomes b, b becomes a+b
        a = (b += a) - a;
    return a;
}

//------------------------------------------------------------------------------

int main(){
    printf("%d\n", climbStairs(5));
}
