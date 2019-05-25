import java.util.*;

class Solution {
    public static int[] twoSum(int[] nums, int target) 
    {
        Map<Integer,Integer> m = new HashMap<>();
        
            for(int i = 0; i < nums.length; i++){
                 m.put(nums[i],i);
            }
            System.out.println(m.size());

            for(int i = 0; i < nums.length; i++)
            {
                if(m.containsValue(target - nums[i] )&& m.get(target - nums[i]) != i)
                {
                    int n[] = new int[]{ m.get(target - nums[i]), i};
                    return n;
                }
            }
        
         throw new IllegalArgumentException("No two sum solution");
    }
    public static void main(String[] args) {
        int nums[] = new int[]{3,3};
        System.out.println(twoSum(nums, 6));

    }
}