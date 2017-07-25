# @param {Integer[]} nums
# @param {Integer} target
# @return {Integer[]}

def two_sum(nums, target)
    map = {}
    nums.each_with_index do |num, index|
        i = map[target - num]
        return [i, index] if i
        map[num] = index
    end
end

#-------------------------------------------------------------------------------
 #Testing

arr = [1, 2, 3, 4]
puts two_sum(arr, 3)
