import java.util.*;
class Solution {
    public static String longestCommonPrefix(String[] strs) 
    {
         if (strs == null || strs.length == 0) return "";
         if(strs.length == 1) return strs[0];
        int prefix = 0 ;
        boolean flag = true ;
        while(flag && prefix < strs[0].length())
        {
            char ch = strs[0].charAt(prefix);
            for(int i = 1; i < strs.length ;i++)
            {
                  if( prefix < strs[i].length())
                {
                    if(ch == strs[i].charAt(prefix))
                    {
                        flag = true;
                    }
                 else{
                     if(prefix == 0)
                     {
                         return "";
                     }
                   flag = false;                  
                 }
                }
            }
            prefix++;  
        }
        return strs[0].length() == 0 ? "" : prefix == 1 ? strs[0].substring(0, 1) :strs[0].substring(0, prefix - 1);
       
    }   
    public static void main(String[] args) {
        String[] strs = new String[]{"flower","flow","flight"};
        System.out.println(longestCommonPrefix(strs));
    }
}