class Solution {
    func isPalindrome(_ x: Int) -> Bool {
        // If x is negative
        if x < 0 {
            return false
        }

        var digits = abs(x)
        // Creates a new number to fill in
        var result = 0
        // Loop through for the amount of digits there are
        while digits > 0 {
            // Create the resulting number in reverse of x
            result = result * 10 + digits % 10
            digits = digits / 10
        }
        // if result is equal to x, it is a palindrome
        return (result == abs(x))

    }
}
