#!/usr/bin/env python3

#-------------------------------------------------------------------------------
class TrieNode:
    # Initialize your data structure here.
    def __init__(self):
        self.children = collections.defaultdict(TrieNode)
        self.is_word = False

class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        current = self.root
        for letter in word:
            current = current.children[letter]
        current.is_word = True

    def search(self, word):
        current = [self.root]
        for letter in word:
            new = []
            for prefix in current:
                if letter == '*':
                    for child in prefix.children:
                        new.append(prefix.children.get(child))
                else:
                    if letter in prefix.children:
                        new.append(prefix.children.get(letter))
            current = new
            if not current:
                return False
            
        for prefix in current:
            if prefix.is_word:
                return True
            
        return False

    def startsWith(self, prefix):
        current = self.root
        for letter in prefix:
            current = current.children.get(letter)
            if current is None:
                return False
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
