import java.util.*;

class solution
{
    public  static int romanToInt(String s) 
    {
           int sum = 0;
            char ch1='0', ch2='0';
            for(int i=0;i<s.length();i++){
                ch1 = s.charAt(i);
                if(i+1<s.length())  ch2 = s.charAt(i+1);
                if(ch1=='I'&& ch2=='V') {sum+=4;i++;continue;}
                if(ch1=='X'&& ch2=='L') {sum+=40;i++;continue;}
                if(ch1=='C'&& ch2=='D') {sum+=400;i++;continue;}
                if(ch1=='I'&& ch2=='X') {sum+=9;i++;continue;}
                if(ch1=='X'&& ch2=='C') {sum+=90;i++;continue;}
                if(ch1=='C'&& ch2=='M') {sum+=900;i++;continue;}
                
                switch(ch1){
                    case 'I': sum += 1;break;
                    case 'V': sum += 5;break;
                    case 'X': sum += 10;break;
                    case 'L': sum += 50;break;
                    case 'C': sum += 100;break;
                    case 'D': sum += 500;break;
                    case 'M': sum += 1000;break;
                }
            }
            return sum;   
            
    }
    public static void main(String[] args)
   {
       String s =  "LVIII";
       System.out.println(romanToInt(s));
        
    }
}