# CTCI 8.4
# Power Set

import copy

#-------------------------------------------------------------------------------
# My Solution
#-------------------------------------------------------------------------------

def power_set(set):
    if set is None:
        return None
    result = []
    get_subset(result, set, len(set)-1)
    return result
    
def get_subset(result, set, idx):
    if idx == -1:
        result.append([])
    else:
        # This goes all the way down until it reaches the base case []
        get_subset(result, set, idx-1)
        # Creates a deep copy of the result to append the next character
        subsets = copy.deepcopy(result)
        for s in subsets:
            s.append(set[idx])
        # Add all the new elements of powerset (idx+1) to the current result
        result.extend(subsets)
        

#-------------------------------------------------------------------------------
#Testing
#-------------------------------------------------------------------------------

print (power_set(['a', 'b', 'c', 'd', 'e']))