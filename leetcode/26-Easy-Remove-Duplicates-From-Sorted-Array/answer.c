#include <stdio.h>
#include <stdlib.h>

//-----------------------------------------------------------------------------

int removeDuplicates(int nums[], int numsSize){
	//If array is empty
        if (numsSize == 0) {
                return 0;
	}
	// Two Pointer Solution
	// j is slow runner, i is fast runner
	int j = 0;
        int i;
	for (i = 1; i < numsSize; i++) {
		// If they are unique change the array and increment
		if (nums[i] != nums[j]) {
			j++;
			nums[j] = nums[i];
		}
	}
	// Return the slow runner + 1 for length
	return j + 1;
}

//-----------------------------------------------------------------------------

int main(){
    int arr[5] = {1, 1, 2, 3, 3};
    printf("%d\n", removeDuplicates(arr, 5));
}
