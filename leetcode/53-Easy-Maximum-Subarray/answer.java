class Solution {
    public int maxSubArray(int[] A) {
        int sum = A[0], max = A[0];
        for(int i = 1; i < A.length; i++){
            // If the sum is less than zero, start a new subarray
            sum = (sum > 0 ? A[i] + sum : A[i]);
            if(sum > max) max = sum;
        }
        return max;
    }
}