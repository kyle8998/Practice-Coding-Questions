#!/usr/bin/python3

#------------------------------------------------------------------------------
# Solution
#------------------------------------------------------------------------------

class Solution:
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        def DFS(row, col, curr):
            # If index in in board dimensions and char is found
            if 0 <= row < len(board) and 0 <= col < len(board[0]) and board[row][col] == word[curr]: 
                # temporarily block out the board to prevent loops
                temp = board[row][col]
                board[row][col] = '#'

                # If we made it to the end of the word, true!
                if curr == len(word)-1:
                    return True

                # Try all four directions
                result = DFS(row-1, col, curr+1) or DFS(row+1, col, curr+1) or DFS(row, col-1, curr+1) or DFS(row, col+1, curr+1)

                # After recursive calls, remove the visited squares for the next attempt
                board[row][col] = temp
                # If we found the entire string in one of the paths return true!
                return result
            else:
                return False
        
        # Iterate through every char and call DFS on all possible first letters
        for row in range(len(board)):
            for col in range(len(board[0])):
                if DFS(row, col, 0):
                    return True
                    
        return False

#------------------------------------------------------------------------------
# Inefficient Solution
# The reason this is more inefficient is that it actually computes the DFS for
# up, down, left, and right before it returns anything. The above solution will
# return True as soon as it finds the string then skip the rest as it is wasted
# work.
#------------------------------------------------------------------------------

class Solution:
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        def DFS(row, col, curr, visited):
            # If char is found
            if board[row][col] == word[curr] and visited[row][col] == 0: 
                visited[row][col] = 1
                if curr == len(word)-1:
                    return True
                
                # Try all four directions
                up, down, left, right = False, False, False, False
                if row > 0:
                    up = DFS(row-1, col, curr+1, visited)
                if row < len(board)-1:
                    down = DFS(row+1, col, curr+1, visited)
                if col > 0:
                    left = DFS(row, col-1, curr+1, visited)
                if col < len(board[0])-1:
                    right = DFS(row, col+1, curr+1, visited)
                    
                # After recursive calls, remove the visited squares for the next attempt
                visited[row][col] = 0
                # If we found the entire string in one of the paths return true!
                return up or down or left or right
            
            else:
                return False
        
        visited = [[0]*len(board[0]) for _ in range(len(board))]
        # Iterate through every char and call DFS on all possible first letters
        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col] == word[0]:
                    if DFS(row, col, 0, visited):
                        return True
                    
        return False
