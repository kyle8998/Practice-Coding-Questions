# CTCI 8.5
# Recursive Multiply

#-------------------------------------------------------------------------------
# My Solution O(logn)
#-------------------------------------------------------------------------------
def mult(n1, n2):
    if n1 > n2:
        a, b = n1, n2
    else:
        a, b = n2, n1
    
    return helper(a, b, {})
    
def helper(big, small, memo):
    if small == 0:
        return 0
    elif small == 1:
        return big
    elif small in memo:
        return memo[small]
        
    # Compute Half
    s = small >> 1
    side1 = helper(big, s, memo)
    side2 = side1
    # If an odd number
    if small % 2 == 1:
        # Actually do the computations out instead of just x2
        side2 = helper(big, small-s, memo)
    # sum and cache
    memo[small] = side1 + side2
    return memo[small]

#-------------------------------------------------------------------------------
# INEFFICIENT SOLUTION O(n)
#-------------------------------------------------------------------------------
def multiply(n1, n2):
    if n1 == 0 or n2 == 0:
        return 0
    return help(n1, n2, 0)


def help(n1, n2, result):
    if n2 == 0:
        return result
    if result == 0:
        result = n1
    else:
        result += n1
    n2 -= 1
    
    return help(n1, n2, result)
#-------------------------------------------------------------------------------
#Testing
#-------------------------------------------------------------------------------

print (mult(9, 5))
print (mult(12, 12))
print (mult(9, 512321))