#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// Stuff above not needed for leetcode submission
//------------------------------------------------------------------------------

// Brute Force, probably very inefficient
int strStr(char* haystack, char* needle) {
    int hay_length = strlen(haystack);
    int needle_length = strlen(needle);
    int i;
    int j;
    int tmp;
    
	// If the needle is an empty string
    if (needle_length == 0) return 0;

	// Loop through the haystack
    for (i = 0; i < hay_length; i++){
		// If the first character is a match
        if (haystack[i] == needle[0]){
            tmp = i;
			// Loop through to see if the string matches
            for (j = 0; j < needle_length; j++){
                if (haystack[tmp] != needle[j]) break;
                if (j == (needle_length - 1)) return i;
                tmp++;
            }
        }
    }
    return -1;
}

//------------------------------------------------------------------------------
// Testing

int main()
{
	printf("%d\n", strStr("string", "ring"));
}
