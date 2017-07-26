func searchInsert(nums []int, target int) int {
    // If target is greater than any value
    if target > nums[len(nums)-1] {
        return len(nums)
    }
    // Loop through array and compare values to target
    for i := 0; i < len(nums); i++{
        if nums[i] >= target {
            return i
        }
    }
    return 0
}