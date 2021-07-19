# fib

# brute force
def fib(n):
    if n <= 2: return 1

    return fib(n-1) + fib(n-2)

# tabulation

def fib(n):
    table = [0] * (n + 1)
    table[1] = 1
    for i in range(n - 1):
        table[i + 1] += table[i]
        table[i + 2] += table[i]
    table[-1] += table[-2]
    return table[-1]

# also

def fib(n):
    if n <= 2: return 1

    prev1, prev2 = 0,1
    output = 0
    for i in range(2, n+1):
        output = prev1 + prev2
        prev2 = prev1
        prev1 = output
    return output


#######################################################################################

# grid traveler , from top left to bottom right, how many ways

def grid_traveller(m, n):
    table = [[0] * (n + 1) for _ in range(m + 1)]
    table[1][1] = 1
    for i in range(1, m):
        for j in range(1, n):
            table[i][j + 1] += table[i][j]
            table[i + 1][j] += table[i][j]
    # right-most column
    for i in range(1, m):
        table[i + 1][-1] += table[i][-1]
    # bottom row
    for j in range(1, n):
        table[-1][j + 1] += table[-1][j]
    return table[m][n]

######################################################################################

def can_sum(targert_sum, numbers):
    table = [False] * (targert_sum + 1)
    table[0] = True
    for i in range(targert_sum):
        if table[i]:
            numbers = [num for num in numbers if i + num <= targert_sum]
            for num in numbers:
                table[i + num] = True
    return table[-1]
