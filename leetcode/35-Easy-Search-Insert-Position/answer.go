
// O(log(n))
func searchInsert(nums []int, target int) int {
    hi := len(nums)-1
    lo := 0
    mid := hi/2
    
    if target > nums[hi] {
        return hi+1
    } 
    
    for lo <= hi {
        if nums[mid]  ==  target{
            return mid			
        }else if nums[mid] < target{
            lo = mid+1			
        }else{
            hi = mid-1		
        }
        mid = (hi-lo) + lo	
    }
    return lo
}

// O(n)
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