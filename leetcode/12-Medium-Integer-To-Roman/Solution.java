class Solution {
    public static String intToRoman(int num) {
        StringBuilder sb = new StringBuilder();
        int values[] = {1000,900,500,400,100,90,50,40,10,9,5,4,1};
        String syms[] = {"M","CM","D","CD","C","XC","L","XL","X","IX","V","IV","I"}; 
        int pnt = 0;
        while (num > 0) {
            if (num >= values[pnt]) {
                sb.append(syms[pnt]);
                num = num - values[pnt];
            } else {
                pnt++;
            }
        }
        return sb.toString();
    }
    public static void main(String[] args)
     {
        System.out.println(intToRoman(1050));
    }
}