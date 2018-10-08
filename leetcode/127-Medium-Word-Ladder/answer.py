#!/usr/bin/env python3

#-------------------------------------------------------------------------------
# Solution
#-------------------------------------------------------------------------------

class Solution:
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        if endWord not in wordList:
            return 0
        
        start = set([beginWord])
        end = set([endWord])
        wordList = set(wordList)
        wordList.discard(beginWord)
        count = 1
        # Iterate and add all possibilities at each point to a stack
        while start:
            temp = []
            if start & end:
                    return count
            # Find all the possible transformations for start
            possible = set()
            for word in start:
                for index in range(len(word)):
                    for c in 'abcdefghijklmnopqrstuvwxyz':
                        possible.add(word[:index] + c + word[index+1:])
            start = wordList & possible
            count += 1
            
            # Swap start and end for optimized bidirectional BFS
            start, end = end, start
            
            wordList -= start
        return 0 

#-------------------------------------------------------------------------------
# First Solution (Time Exceeded)
#-------------------------------------------------------------------------------

class Solution:
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        def isOneAway(word1, word2):
            """
            Determine if a word can be transformed with a single char change
            """
            count = 0
            for i in range(len(word1)):
                if word1[i] != word2[i]:
                    count += 1
            return count == 1
        
        words = [beginWord]
        count = 1
        # Iterate and add all possibilities at each point to a stack
        while words:
            temp = []
            # For every word in the stack, find all possible transformations at that point
            for word in words:
                # If found return count
                if word == endWord:
                    return count
                # Attempt transformations with the remaining dict words
                for dictword in wordList:
                    if isOneAway(word, dictword):
                        wordList.remove(dictword)
                        temp.append(dictword)
            # Replace the stack with the new transformed stack!
            words = temp
            count += 1
        return 0
                    
#-------------------------------------------------------------------------------
