#include <stdio.h>
#include <string.h>

int romanToInt(char* s) {
    int i;
    int result = 0;
    // Loop through characters
    for (i = 0; i < strlen(s); i++){
        // Switch statements for the basic numeral values
        // Multiples of 10 are special as they can be subtracted
        switch (s[i]){
            case 'M':
                result += 1000;
                break;
            case 'D':
                result += 500;
                break;
            case 'C':
                if (s[i+1] == 'D' || s[i+1] == 'M') result -= 100;
                else result += 100;
                break;
            case 'L':
                result += 50;
                break;
            case 'X':
                if (s[i+1] == 'L' || s[i+1] == 'C') result -= 10;
                else result += 10;
                break;
            case 'V':
                result += 5;
                break;
            case 'I':
                if (s[i+1] == 'V' || s[i+1] == 'X') result--;
                else result++;
                break;
        }
    }
    return result;
}

//------------------------------------------------------------------------------

int main(){
    printf("%d\n", romanToInt("XXX"));
}
