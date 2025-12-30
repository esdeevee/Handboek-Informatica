def fibonacci_iteratief(n):
    a = 1
    b = 1
    for i in range(1, n):
        c = a+b
        a = b
        b = c
    return a

def fibonacci_recursief(n):
    if n <= 2:
        return 1
    else:
        return fibonacci_recursief(n-1) + fibonacci_recursief(n-2)
