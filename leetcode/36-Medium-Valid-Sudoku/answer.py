#!/usr/bin/python

#------------------------------------------------------------------------------

class Solution:
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        
        list = []
        # Check columns
        for i in range(9):
            for j in range (9):
                curr = board[i][j]
                if curr != '.':
                    if curr not in list:
                        list.append(curr)
                        
                    else:
                        return False
            list.clear()
            
        # Check rows
        for j in range(9):
            for i in range (9):
                curr = board[i][j]
                if curr != '.':
                    if curr not in list:
                        list.append(curr)
                        
                    else:
                        return False
            list.clear()
            
        # Check 3x3 boxes
        for r in range(0, 9, 3):
            for d in range(0, 9, 3):
                for i in range(r, r+3):
                    for j in range(d, d+3):
                        curr = board[i][j]
                        if curr != '.':
                            if curr not in list:
                                list.append(curr)
                        
                            else:
                                return False
                list.clear()
            
        return True

#------------------------------------------------------------------------------
#Testing
