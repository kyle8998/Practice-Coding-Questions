#!/usr/bin/python

#------------------------------------------------------------------------------

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        length = len(strs)
        result = ""
        charsleft = True
        i = -1
        # Check if array is empty
        if length > 0:
            # Really silly way to ensure that there are no blank strings
            # Definitely not optimal, but I was lazy
            for string in strs:
                if len(string) == 0:
                    return result

            # Loop while there are characters left
            while charsleft:
                # Increment index
                i += 1
                if len(strs[0]) == i:
                    return result
                char = strs[0][i]
                # Loop through the character in each string
                for index in range(1, length):
                    # If the character is not the same, return result
                    if not strs[index][i] == char:
                        return result
                    # If it is at the end of the string
                    if len(strs[index]) == i + 1:
                        charsleft = False
                # Concatenate string
                result += char

        return result

#------------------------------------------------------------------------------
#Testing

def main():
    x = Solution()
    y = x.longestCommonPrefix(["hello", "hello", "hello"])
    print y

    print Solution().longestCommonPrefix(["abc", "absdfsf", "ab"])
    print Solution().longestCommonPrefix(["woahsomany", "woah", "woahvenrui"])
    print Solution().longestCommonPrefix([])
    print Solution().longestCommonPrefix(["", "ab", "a"])
    print Solution().longestCommonPrefix(["a", "ab", "ab"])



main()
