/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number}
 */
var searchInsert = function(nums, target) {
    // Set variables to the left and right most parts of array
    var left = 0;
    var right = nums.length - 1;
    // While there are more elements
    while(left <= right){
        // Find midpoint
        var mid = parseInt((left + right)/2);
        var val = nums[mid];
        // If the value is the target, return it
        if(val === target){
            return mid;
        } 
        // If it is greater than, find mid point of second half
        else if(val > target){
            right = mid - 1;
        } 
        // If it is less than, find mid point of first half
        else {
            left = mid + 1;
        }
    }
    // If the target is not in the array
    if(nums[left] < target){
        return left + 1;
    } else {
        return left;
    }
};