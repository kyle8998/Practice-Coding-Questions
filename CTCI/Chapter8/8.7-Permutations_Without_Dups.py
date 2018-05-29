# CTCI 8.7
# Permutations Without Dups

#-------------------------------------------------------------------------------
# My Solution 
#-------------------------------------------------------------------------------

def perm(str):
    if str == None:
        return None
        
    result = []
    if len(str) == 0:
        result.append("")
        return result
        
    first = str[0]
    remainder = str[1:len(str)]
    
    # This recursively gets permutations from the remainder, so it starts at the empty string
    permutations = perm(remainder)
    
    # For every permutations
    for word in permutations:
        # For every possible index in each permutation
        for i in range(len(word)+1):
            # Add the new letter to every index to generate new set of permutations
            result.append(insertAt(word, first, i))

    return result
    
        

def insertAt(str, c, idx):
    return str[:idx] + c + str[idx:len(str)]

#-------------------------------------------------------------------------------
#Testing
#-------------------------------------------------------------------------------
print(perm("abcde"))
