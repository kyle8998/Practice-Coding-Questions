#include <stdio.h>

int main(void) {
    // Set n which will take user input to 0
    int n=0;
    // Loop to continue to take user input intil n is 42
    while(n != 42){
        // Take user input
        scanf("%d", &n);
        // If user input is 42, do not print and exit
        if (n !=42)
            printf("%d\n", n);
    }
    return(0);
}
