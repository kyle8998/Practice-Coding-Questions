import java.util.*;

public class Solution 
{
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) 
    {  
     return adder(l1,l2,0);   
    }
    public ListNode adder(ListNode l1, ListNode l2, int carry) 
    {  
       if (l1 == null && l2 == null ) 
       {
            if (carry == 0) 
                return null;
            else 
                return new ListNode(1);
        }
        int sum = (l1 == null ? 0: l1.val) + (l2 == null ? 0: l2.val) + carry;
        ListNode result = new ListNode(sum % 10);
        result.next = adder((l1==null ? null : l1.next),(l2==null ? null : l2.next),sum/10);
            
        return result;
        
    }

    /// testing
    public static void main(String[] args) 
    {
        int num1 = 342;
        int num2 = 465;
        int n = num1 % 10;             // n = 2
        ListNode l1 = new ListNode(n);
        ListNode node1 = l1;
        num1 = num1 /10;
        while(num1 > 0)
        {
            n = num1 % 10;
            node1.next = new ListNode(n);
            num1 = num1 / 10;
            node1 = node1.next;
        }
        n = num2 % 10;            // n = 5
        ListNode l2= new ListNode(n);
        ListNode node2 = l2;
        num2 = num2 /10;
        while(num2 > 0)
        {
            n = num2 % 10;
            node2.next = new ListNode(n);
            num2 = num2 / 10;
            node2 = node2.next;
        }
        Solution s = new Solution();

        // calling function  addTwoNumber , it will return result linkedlist ...........
        ListNode result = s.addTwoNumbers(l1, l2);

        /// printing input linkedlist 1...........
        System.out.print("Input :  ");
        while(l1.next!= null)
        {
            System.out.print((l1 == null ? "": l1.val+"->"));
            l1 = l1.next;
           
        }
        System.out.print(l1 != null ? l1.val : "");

        /// printing input linkedlist 2.............

        System.out.print(" + ");

        while(l2.next != null)
        {
            System.out.print((l2 == null ? "": l2.val+"->"));
            l2 = l2.next;
        }
        System.out.println(l2 != null ? l2.val : "");

        //printing result linkedlist............
        System.out.print("Output : ");
        while(result.next != null)
        {
            System.out.print(result.val +"->");
            result = result.next;
        }
        System.out.println(result != null ? result.val : "");
        
    }
    
}
class ListNode {
    int val;
    ListNode next;
    ListNode(int x) { val = x; }
    }

