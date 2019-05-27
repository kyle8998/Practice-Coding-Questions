class Solution {
    public int reverse(int x) 
    {
        int rev = 0,n = 0 ;
        boolean neg = false;
        if( x < 0)
        {
            x = x * -1;
            neg = true;
        }
        while( x > 0)
        {
            n = x % 10;
            if (rev > Integer.MAX_VALUE/10 || (rev == Integer.MAX_VALUE / 10 && n > 7)) return 0;
            if (rev < Integer.MIN_VALUE/10 || (rev == Integer.MIN_VALUE / 10 && n < -8)) return 0;
            rev = rev * 10 + n;
            x = x / 10;
            
        }
        if(neg){ rev = -1 * rev ;}
        return rev;
    }
     public static void main(String[] args)
      {
        Solution s = new Solution();
        System.out.println(s.reverse(324));
     }
}