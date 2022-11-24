def Fib(n):
    import numpy as np
    n: int
    fib = np.array([1, 1])
    for i in range(1, n-1):
        fib = np.append(fib, [fib[-1] + fib[-2]])
    return(fib)

def Sort(a):
    for i in range(len(a)):
         for j in range(len(a)-1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
    return(a)

def Calc(a, b, s):
    if s == '+':
        return a+b
    if s == '-':
        return a-b
    if s == '*':
        return a*b
    if s == '/':
        return a/b