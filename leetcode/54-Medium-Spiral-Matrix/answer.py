#!/usr/bin/python

#------------------------------------------------------------------------------

class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        
        result = []
        
        if len(matrix) == 0: return result
        
        # Limits set for spiral
        hlimit = len(matrix[0])
        vlimit = len(matrix) - 1
        
        # Indexes set to keep track of the spiral
        hidx = 0
        vidx = 0
        
        # Curr to count amount of times iterated
        curr = 0
        
        # Weird triggers to break loop for nonsquare arrays
        # Probably a bad way to go about it, but I'm tired right now
        vTrigger = True
        hTrigger = True
        
        # Each loop is one full spiral around the array
        while hlimit > 0 or vlimit > 0:
            ## Forward
            # Horizontal
            if not vTrigger: break
            while curr < hlimit:
                result.append(matrix[vidx][hidx])
                hidx += 1
                curr += 1
                hTrigger = True
                
            # Sets hidx back to proper position
            hidx -= 1
            # Moves down for next loop
            vidx += 1
            hlimit -= 1
            curr = 0
            vTrigger = False
                
            # Vertical
            if not hTrigger: break
            while curr < vlimit:
                result.append(matrix[vidx][hidx])
                vidx += 1
                curr += 1
                vTrigger = True
                
            # Set vidx back to proper position
            vidx -= 1
            # Moves to the left for the next loop
            hidx -= 1
            vlimit -= 1
            curr = 0
            hTrigger = False
        
            ## Backwards
            # Horizontal
            if not vTrigger: break
            while curr < hlimit:
                result.append(matrix[vidx][hidx])
                hidx -= 1
                curr += 1
                hTrigger = True
                
            # Set hidx back to proper position
            hidx += 1
            # Moves up for the next loop
            vidx -= 1
            hlimit -= 1
            curr = 0
            vTrigger = False
            
            # Vertical
            if not hTrigger: break
            while curr < vlimit:
                result.append(matrix[vidx][hidx])
                vidx -= 1
                curr += 1
                vTrigger = True
                
            # Set vidx back to proper position
            vidx += 1
            # Moves right for the next loop
            hidx += 1
            vlimit -= 1
            curr = 0
            hTrigger = False
        
        return result

#------------------------------------------------------------------------------
#Testing

def main():
    print Solution().spiralOrder([[2,3]])




main()
