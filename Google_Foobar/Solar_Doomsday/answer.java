package com.google.challenges; 

public class Answer {   
    public static int[] answer(int area) { 

        // Your code goes here.
        int[] data = new int[0];
        return helper(data, area, 1);
        
    } 
    
    // Helper method for recursion
    public static int[] helper(int[] arr, int area, int size) { 
        // Base case, area is 0
        if(area == 0) return arr;
        // Create new array 1 size larger
        int[] data = new int[size];
        int idx = 0;
        // Fill array with previous contents
        for(int num:arr){
            data[idx] = num;
            idx++;
        }
        // Find the square root and round it to find the difference
        int root = (int) Math.sqrt(area);
        int square = root * root;
        int difference = area - square;
        // Set the new idx equal to the area of the square
        data[idx] = square;
        
        return helper(data, difference, size + 1);
    }
}