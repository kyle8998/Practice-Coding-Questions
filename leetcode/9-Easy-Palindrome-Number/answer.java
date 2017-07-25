public class Solution {
    public boolean isPalindrome(int x) {

        int temp = x, digits = 1;
        // If x is negative
        if (x < 0)
            return false;

        // Find 1^digits
        while (temp >= 10){
            temp /= 10;
            digits *= 10;
        }

        // While there are numbers left
        while (x > 0){
            if ((x % 10) != (x / digits))
                return false;
            // Removes a digit off each side
            x = (x % digits) / 10;
            // Removes 2 digits
            digits /= 100;
        }
        return true;
    }
}

//-----------------------------------------------------------------------------

public static void main(String[] args){
        system.out.println(isPalindrome(1234321));
}
