import java.util.*;

class Solution {
  /*  public static int removeDuplicates(int[] nums)
    { 
         LinkedHashSet<Integer> hs = new LinkedHashSet<>();
        int j = 0;
        for(int i = 0 ; i < nums.length; i++)
        {
           if( hs.add(nums[i]))
           {
              nums[j] = nums[i]; 
               j++;
           }
           
        }
        return hs.size();
        
    }
    */
    public static int removeDuplicates(int[] nums)
    {
        int j = 0;
        for(int i = 1 ; i< nums.length; i++)
        {
            if(nums[j] != nums[i])
            {
                 j++;
             nums[j] = nums[i];
               
            }
        }
        return j + 1;
        
    }
    public static void main(String[] args) {
        int[] nums = new int[]{0,0,1,1,1,2,2,3,3,4};
        System.out.println(removeDuplicates(nums));
    }
}