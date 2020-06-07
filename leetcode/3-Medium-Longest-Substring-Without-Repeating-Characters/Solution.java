import java.util.*;
class Solution {

    public static int lengthOfLongestSubstring(String s) 
    {
    int i = 0, j = 0, max = 0;
    HashSet<Character> set = new HashSet<>();
    
    while (j < s.length()) {
        if (!set.contains(s.charAt(j))) {
            set.add(s.charAt(j++));
            max = Math.max(max, set.size());
        } else {
            set.remove(s.charAt(i++));
        }
    }
    
    return max;
    }
    
    ////.................TESTING................./////

    public static void main(String[] args) 
    {
        String s = "dvdf";
        System.out.println("Input : "+ s);
        System.out.println("Output : "+lengthOfLongestSubstring(s));

    }
}
