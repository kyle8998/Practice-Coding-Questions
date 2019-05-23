import java.util.*;

class add_two_number
{
    node start;
    public void append(int d)
    {
        node temp = new node(d);
        if(this.start == null)
        {
          this.start = temp;
        }
        else
        {
          node pos = new node();
          pos = this.start;
          while(pos.next != null)
          {
              pos = pos.next;
          }
          pos.next = temp;
        }
    
    }

    public void printlist()
    {
        node pos = new node();
        pos = this.start;
        while(pos!= null)
          {
              System.out.println(pos.data);
              pos = pos.next;
          }
    }

   public static void main(String[] args)
   {
       Scanner sc =  new Scanner(System.in);
       add_two_number linkedlist1 = new add_two_number();
       add_two_number linkedlist2 = new add_two_number();
       add_two_number result = new add_two_number();
       int num1 = sc.nextInt();
       int num2 = sc.nextInt();
       while(num1 > 0)
       {
           int n = num1 % 10;
           linkedlist1.append(n);
           num1 = num1 / 10;
       }
       System.out.println("first number");
       linkedlist1.printlist();
       while(num2 > 0)
       {
           int n = num2 % 10;
           linkedlist2.append(n);
           num2 = num2 / 10;
       }
       System.out.println("second number");
       linkedlist2.printlist();
       node pos = new node();
        pos = linkedlist1.start;
        int i = 1 ,n1 = 0;
        while(pos!= null)
          {
              n1 = n1 + pos.data * i;
              pos = pos.next;
              i = i * 10;
          }
        pos = linkedlist2.start;
        int j = 1 ,n2 = 0;
        while(pos!= null)
          {
              n2 = n2 + pos.data * j;
              pos = pos.next;
              j = j * 10;
          }
          int sum = n1 + n2;
          while(sum > 0)
          {
              int n = sum % 10;
              result.append(n);
              sum = sum / 10;
          }
          System.out.println("result linledlist");
          result.printlist();
   }
   
}
class node
   {
       int data;
       node next;
       public node(int d)
       {
           this.data = d;
       }
       public node(){}
   
   }