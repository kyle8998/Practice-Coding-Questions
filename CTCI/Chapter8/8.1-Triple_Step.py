# CTCI 8.1
# Triple Step

#-------------------------------------------------------------------------------
# My Solution
#-------------------------------------------------------------------------------

# BRUTE FORCE O(3^n)
def triple_step_brute(n):
    if n == 0:
        return 1
    if n < 0:
        return 0
    return triple_step_brute(n-1) + triple_step_brute(n-2) + triple_step_brute(n-3)

# DP Way
# Caches values that are already seen

def triple_step(n):
    return helper(n, [-1]*(n+1))
    
def helper(n, memo):
    if n < 0:
        return 0

    memo[0] = 1

    if n >= 1:
        memo[1] = 1
    if n >= 2:
        memo[2] = memo[1] + memo[0]
    if n > 2:
        for i in range(3, n + 1):
            memo[i] = memo[i - 1] + memo[i - 2] + memo[i - 3]
    return memo[n]

#-------------------------------------------------------------------------------
#Testing
#-------------------------------------------------------------------------------
for i in range(10):
    print(triple_step(i))