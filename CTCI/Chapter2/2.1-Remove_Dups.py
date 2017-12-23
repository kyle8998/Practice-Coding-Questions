# CTCI 2.1
# Remove Dups

import unittest
# Uh this isn't working?
from LinkedList import LinkedList


# My Solution

def remove_dups(head):
    unique = []

    # Initialize prev and curr - return if 1 or 0 element list
    if head and head.next:
        prev = head
        curr = head.next
        unique.append(prev.val)
    else:
        return head

    # Iterate through list adding each unique value to the list
    while curr:
        if curr.val not in unique:
            unique.append(curr.val)
            curr = curr.next
            prev = prev.next
        else:
            curr = curr.next
            prev.next = curr

    return head

#-------------------------------------------------------------------------------
# CTCI Solution

def remove_dups2(ll):
    if ll.head is None:
        return

    current = ll.head
    seen = set([current.value])
    while current.next:
        if current.next.value in seen:
            current.next = current.next.next
        else:
            seen.add(current.next.value)
            current = current.next

    return ll


def remove_dups_followup(ll):
    if ll.head is None:
        return

    current = ll.head
    while current:
        runner = current
        while runner.next:
            if runner.next.value == current.value:
                runner.next = runner.next.next
            else:
                runner = runner.next
        current = current.next

    return ll.head

#-------------------------------------------------------------------------------
#Testing

ll = LinkedList()
ll.generate(100, 0, 9)
print(ll)
remove_dups(ll)
print(ll)

ll.generate(100, 0, 9)
print(ll)
remove_dups_followup(ll)
print(ll)
