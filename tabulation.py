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
