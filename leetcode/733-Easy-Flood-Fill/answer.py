#!/usr/bin/env python

#-------------------------------------------------------------------------------
class Solution:
    def floodFill(self, image, sr, sc, newColor):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type newColor: int
        :rtype: List[List[int]]
        """
        if sr >= 0 and sr < len(image) and sc>=0 and sc < len(image[0]):
            visited = [[0 for x in range(len(image[0]))] for y in range(len(image))] 
            color = image[sr][sc]
            neighbors = [(sr, sc)]

            while neighbors:
                x, y = neighbors.pop()
                visited[x][y] = 1

                # Change color and then find all new neighbors
                if image[x][y] == color:
                    image[x][y] = newColor
                    if x-1 >= 0 and visited[x-1][y] == 0:
                        neighbors.append((x-1, y))
                    if x+1 < len(image) and visited[x+1][y] == 0:
                        neighbors.append((x+1, y))
                    if y-1 >= 0 and visited[x][y-1] == 0:
                        neighbors.append((x, y-1))
                    if y+1 < len(image[0]) and visited[x][y+1] == 0:
                        neighbors.append((x, y+1))
          
        return image
#-------------------------------------------------------------------------------
# Testing
