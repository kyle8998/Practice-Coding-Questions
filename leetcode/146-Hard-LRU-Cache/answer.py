#!/usr/bin/env python3

#-------------------------------------------------------------------------------
# First Inefficient Solution O(n) operations
#-------------------------------------------------------------------------------

class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.cache = {}
        self.recent_list = []
        self.capacity = capacity
        

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.cache:
            self.recent_list.remove(key)
            self.recent_list.append(key)
            return self.cache[key]
        else:
            return -1
        

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if key in self.recent_list:
            self.recent_list.remove(key)
            self.recent_list.append(key)
        elif len(self.recent_list) == self.capacity:
            del self.cache[self.recent_list.pop(0)]
            self.recent_list.append(key)
        else:
            self.recent_list.append(key)
        self.cache[key] = value


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)  

#-------------------------------------------------------------------------------
# O(1) Operations using a doubly linked list
#-------------------------------------------------------------------------------

class Node(object):
    def __init__(self, key, value):
        self.key = key
        self.val = value
        self.prev = None
        self.next = None

class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.cache = {}
        # We will have a dummy head and tail so the list will always be in between
        self.tail = Node(0,0)
        self.head = Node(0,0)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.capacity = capacity
        

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        # Remove and add from linked list
        if key in self.cache:
            node = self.cache[key]
            self._remove(node)
            self._add(node)
            return node.val
        else:
            return -1
        

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        # If key exists, update value then update linkedlist
        if key in self.cache:
            node = self.cache[key]
            node.val = value
            self._remove(node)
            self._add(node)
        # Else create the new node and append and remove least recently used if necessary
        else:
            node = Node(key, value)
            self._add(node)
            self.cache[key] = node
            if len(self.cache) > self.capacity:
                del self.cache[self.tail.prev.key]
                self._remove(self.tail.prev)
                
        
    def _remove(self, node):
        node.prev.next, node.next.prev = node.next, node.prev
        
    def _add(self, node):
        #self.head.next, node.next, node.prev, self.head.next.prev = node, self.head.next, self.head, node
        n1 = self.head.next
        self.head.next = node
        node.next = n1
        n1.prev = node
        node.prev = self.head
        return
#-------------------------------------------------------------------------------

