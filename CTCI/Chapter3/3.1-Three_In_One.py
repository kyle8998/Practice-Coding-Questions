# CTCI 3.1
# Three in One

import unittest

class ThreeStacks():
    def __init__(self):
        self.array = [None, None, None]
        self.current = [0, 1, 2]
        
    def push(self, item, stack_number):
        if not stack_number in [0, 1, 2]:
            raise Exception("Bad stack number")
        while len(self.array) <= self.current[stack_number]:
            self.array += [None] * len(self.array)
        self.array[self.current[stack_number]] = item
        self.current[stack_number] += 3
    
    def pop(self, stack_number):
        if not stack_number in [0, 1, 2]:
            raise Exception("Bad stack number")
        if self.current[stack_number] > 3:
            self.current[stack_number] -= 3
        item = self.array[self.current[stack_number]]
        self.array[self.current[stack_number]] = None
        return item
    

#-------------------------------------------------------------------------------
# CTCI Solution 

class MultiStack:

    def __init__(self, stacksize):
        self.numstacks = 3
        self.array = [0] * (stacksize * self.numstacks)
        self.sizes = [0] * self.numstacks
        self.stacksize = stacksize

    def Push(self, item, stacknum):
        if self.IsFull(stacknum):
            raise Exception('Stack is full')
        self.sizes[stacknum] += 1
        self.array[self.IndexOfTop(stacknum)] = item

    def Pop(self, stacknum):
        if self.IsEmpty(stacknum):
            raise Exception('Stack is empty')
        value = self.array[self.IndexOfTop(stacknum)]
        self.array[self.IndexOfTop(stacknum)] = 0
        self.sizes[stacknum] -= 1
        return value

    def Peek(self, stacknum):
        if self.IsEmpty(stacknum):
            raise Exception('Stack is empty')
        return self.array[self.IndexOfTop(stacknum)]

    def IsEmpty(self, stacknum):
        return self.sizes[stacknum] == 0

    def IsFull(self, stacknum):
        return self.sizes[stacknum] == self.stacksize

    def IndexOfTop(self, stacknum):
        offset = stacknum * self.stacksize
        return offset + self.sizes[stacknum] - 1

#-------------------------------------------------------------------------------
#Testing

class Test(unittest.TestCase):
  def test_three_stacks(self):
    three_stacks = ThreeStacks()
    three_stacks.push(101, 0)
    three_stacks.push(102, 0)
    three_stacks.push(103, 0)
    three_stacks.push(201, 1)
    self.assertEqual(three_stacks.pop(0), 103)
    self.assertEqual(three_stacks.pop(1), 201)
    self.assertEqual(three_stacks.pop(1), None)
    self.assertEqual(three_stacks.pop(2), None)
    three_stacks.push(301, 2)
    three_stacks.push(302, 2)
    self.assertEqual(three_stacks.pop(2), 302)
    self.assertEqual(three_stacks.pop(2), 301)
    self.assertEqual(three_stacks.pop(2), None)

if __name__ == "__main__":
  unittest.main()