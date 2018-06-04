# CTCI 8.8
# Permutations With Dups

#-------------------------------------------------------------------------------
# My Solution 
#-------------------------------------------------------------------------------
# Only generates new permutations using freq list
#-------------------------------------------------------------------------------

def perm_no_dups(str):
    freq_list = build_freq(str)
    return perm_help(freq_list, "", len(str), [])

# Build freq list
def build_freq(str):
    result = {}
    for c in str:
        if c in result:
            result[c] += 1
        else:
            result[c] = 1
    return result
    
# Do all perm generation here
def perm_help(freq_list, prefix, remaining, result):
    # If all characters used
    if remaining == 0:
        result.append(prefix)
        return result
    
    # Loop through all possible letters to use
    for c in freq_list.keys():
        count = freq_list[c]
        # If # in freq list > 0
        if count > 0:
            freq_list[c] -= 1
            # Add the char to the prefix
            # This will generate all possible prefixes
            perm_help(freq_list, prefix+c, remaining-1, result)
            # Add all the characters back for the next loop
            freq_list[c] += 1
            
    return result

#-------------------------------------------------------------------------------
# Less efficient way
# Always runs n! because it generates dups
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
            newperm = insertAt(word, first, i)
            
            if newperm not in result:
                result.append(newperm)

    return result
    
        

def insertAt(str, c, idx):
    return str[:idx] + c + str[idx:len(str)]

#-------------------------------------------------------------------------------
#Testing
#-------------------------------------------------------------------------------
print(perm_no_dups("aabb"))
