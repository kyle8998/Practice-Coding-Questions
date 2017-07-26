object Solution {
    def searchInsert(nums: Array[Int], target: Int): Int = {
        // If target is greater than any value
        if (target > nums(nums.length - 1)){
            return nums.length;
        }
        // Loop through array and compare values to target
        for( i <- 0 until nums.length){
            if (nums(i) >= target){
                return i;
            }
        }
        return 0;
    }
}