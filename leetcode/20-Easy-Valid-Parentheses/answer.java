public class Solution {
    public boolean isValid(String s) {
        Stack<Character> stack = new Stack<Character>();
        // Iterate through string
        for(int i = 0; i < s.length(); i++){
            // Put opening into stack
            if(s.charAt(i) == '(' || s.charAt(i) == '{' || s.charAt(i) == '[')
                stack.push(s.charAt(i));
            // If it is a closing character, pop from stack if matches
            else if((s.charAt(i) == ')' && !stack.empty() && stack.peek() == '(') ||
                    (s.charAt(i) == '}' && !stack.empty() && stack.peek() == '{') ||
                    (s.charAt(i) == ']' && !stack.empty() && stack.peek() == '['))
                stack.pop();
            // Else it is not valid
            else return false;
        }
        return stack.empty();
    }
}
