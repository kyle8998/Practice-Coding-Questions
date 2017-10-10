import java.util.*;
import java.math.*;

public class Arithmetic {

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        double mealCost = scan.nextDouble(); // original meal price
        int tipPercent = scan.nextInt(); // tip percentage
        int taxPercent = scan.nextInt(); // tax percentage
        scan.close();
      
        // Write your calculation code here.
      
        // cast the result of the rounding operation to an int and save it as totalCost 
        int totalCost = (int) Math.round(mealCost + 
                                      (mealCost * ((double)tipPercent / 100)) +
                                      (mealCost * ((double)taxPercent / 100)));
        // Print your result
        System.out.println("The total meal cost is " + totalCost + " dollars.");
    }
}