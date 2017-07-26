public class Solution {
    public int searchInsert(int[] nums, int target) {
        // If target is greater than any value
        if (target > nums[nums.length-1])
            return nums.length;
        // Loop through array and compare values to target
        for (int i = 0; i < nums.length; i++){
            if (nums[i] >= target){
                return i;
            }
        }
        return 0;
    }
}