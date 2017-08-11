public class Solution {
    public static String convert(String s, int numRows) {
	    // If there is only 1 row
	        if (numRows <= 1)
	        	return s;
        // Create string buffer to hold string buffer for each row
	    StringBuffer[] result = new StringBuffer[numRows];
	    for (int i = 0; i < numRows; i++){
	        result[i] = new StringBuffer();
	    }
	    // Trigger to make it traverse up and down rows
	    boolean up = true;
	    int row = 0;
	    // Loops through string
	    for (int i = 0; i < s.length(); i++){
	        result[row].append(s.charAt(i));
	        // Go up and down when necessary
	        if(up) row++;
	        else row--;
	        // Trigger when necessary
	        if(row == numRows - 1) up = false;
	        else if(row == 0) up = true;
	    }
	    // Append results to the first string buffer
	    for (int i = 1; i < result.length; i++){
	        result[0].append(result[i]);
	    }
	    return result[0].toString();
	}
}