#!/bin/python3

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None 
class Solution: 
    def insert(self,head,data):
            p = Node(data)           
            if head==None:
                head=p
            elif head.next==None:
                head.next=p
            else:
                start=head
                while(start.next!=None):
                    start=start.next
                start.next=p
            return head  
    def display(self,head):
        current = head
        while current:
            print(current.data,end=' ')
            current = current.next
            
    def removeDuplicates(self,head):
        #Write your code here
        
        # Elements array to keep track of unique elements
        # This way is less memory efficient but more time efficient
        elements = []
        curr = head

        if curr is not None:
            elements.append(curr.data)

        while curr is not None and curr.next is not None:
            if curr.next.data not in elements:
                elements.append(curr.next.data)
                curr = curr.next
            else:
                curr.next = curr.next.next

        return head
        
mylist= Solution()
T=int(input())
head=None
for i in range(T):
    data=int(input())
    head=mylist.insert(head,data)    
head=mylist.removeDuplicates(head)
mylist.display(head); 