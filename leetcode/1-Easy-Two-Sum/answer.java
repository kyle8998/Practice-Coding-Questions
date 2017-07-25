public class Solution {
    public int[] twoSum(int[] nums, int target) {
        // Loop Through Array in Nested Loops
        for (int i=0; i<nums.length; i++){
            for (int j=0; j<nums.length; j++){
                // If indices are equal skip loop
                if (i == j)
                    continue;
                // If it equals the target, return the indices
                if ((nums[i]+nums[j]) == target){
                    return new int[] { i, j };
                }
            }
        }
        throw new IllegalArgumentException();
    }
}