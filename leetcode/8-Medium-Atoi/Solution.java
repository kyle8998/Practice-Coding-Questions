import java.util.*;

class Solution {
    public static int myAtoi(String str) 
    {
        int num = 0;
        int d = 10, neg = 1;
        boolean digit_occur = false;
        for(int i = 0 ; i < str.length(); i++) {

            char ch = str.charAt(i);
            if(Character.isAlphabetic(ch) || ch == '.' || ch == '-' || ch ==' ' || ch == '+'){
                if(digit_occur ){
                    return neg * num;
                }
                else{
                     if (ch == ' ' || ch == '+' || ch == '-'){
                        if(i+ 1 < str.length())
                        {
                           if(Character.isDigit(str.charAt(i+1)))
                           { neg = ch == '-' ? neg * -1 : neg ;}
                            else if (ch == ' ') {
                                continue;
                            }
                            else 
                            {return neg * num;}
                            
                        }
                       
                    }
                    else 
                    {
                        return neg * num;
                    }
                }
            }
            if(Character.isDigit(ch)){
                digit_occur = true;
                  if (num > Integer.MAX_VALUE/ 10 || num == Integer.MAX_VALUE  /10 && Integer.MAX_VALUE % 10 < (ch - '0') ) {
                      return neg == 1 ? Integer.MAX_VALUE  : Integer.MIN_VALUE;}
                  num = num * d + Character.getNumericValue(ch);
            }
            
        }
           
        return neg *num;
        
    }
    public static void main(String[] args) 
    {
    
        String s = ".1";
        System.out.println( myAtoi(s));
    }
}