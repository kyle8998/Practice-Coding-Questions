# CTCI 2.5
# Sum Lists

import unittest
#from LinkedList import LinkedList

# My Solution
    
def sum_lists(num1, num2):
    # Curr3 will be a slow runner for curr1 for the result instead of creating a new list
    curr1, curr2, curr3 = num1, num2, num1
    rem = 0
    
    # While there are elements left or there is a remainder
    while curr1 or curr2 or rem:
        sum = rem
        
        if curr1:
            sum += curr1.data
            curr1 = curr1.next
        if curr2:
            sum += curr2.data
            curr2 = curr2.next
            
        rem = 0
        if sum > 10:
            rem = 1
            # subtraction cheaper than modulus
            sum -= 10
            
        curr3.data = sum
        curr3 = curr3.next
        
    # Adds a Null at the end just to be safe!
    if curr3:
        curr3.next = None
        
    return num1
    


#-------------------------------------------------------------------------------
# CTCI Solution

def asum_lists(ll_a, ll_b):
    n1, n2 = ll_a.head, ll_b.head
    ll = LinkedList()
    carry = 0
    while n1 or n2:
        result = carry
        if n1:
            result += n1.value
            n1 = n1.next
        if n2:
            result += n2.value
            n2 = n2.next

        ll.add(result % 10)
        carry = result // 10

    if carry:
        ll.add(carry)

    return ll


def sum_lists_followup(ll_a, ll_b):
    # Pad the shorter list with zeros
    if len(ll_a) < len(ll_b):
        for i in range(len(ll_b) - len(ll_a)):
            ll_a.add_to_beginning(0)
    else:
        for i in range(len(ll_a) - len(ll_b)):
            ll_b.add_to_beginning(0)

    # Find sum
    n1, n2 = ll_a.head, ll_b.head
    result = 0
    while n1 and n2:
        result = (result * 10) + n1.value + n2.value
        n1 = n1.next
        n2 = n2.next

    # Create new linked list
    ll = LinkedList()
    ll.add_multiple([int(i) for i in str(result)])

    return ll

#-------------------------------------------------------------------------------
#Testing

class Node():
  def __init__(self, data, next=None):
    self.data, self.next = data, next
  
  def __str__(self):
    string = str(self.data)
    if self.next:
      string += ',' + str(self.next)
    return string
    
class Test(unittest.TestCase):
  def test_sum_lists(self):
    num1 = Node(1,Node(2,Node(3)))
    num2 = Node(4,Node(9,Node(5)))
    self.assertEqual(str(sum_lists(num1, num2)), "5,1,9")
    num1 = Node(9,Node(2,Node(3,Node(4,Node(1)))))
    num2 = Node(4,Node(9,Node(8)))
    self.assertEqual(str(sum_lists(num1, num2)), "3,2,2,5,1")

if __name__ == "__main__":
  unittest.main()