def tribonacci_recursief(a, b, c, n):
    if n == 1:
        return a
    if n == 2:
        return b
    if n == 3:
        return c
    else:
        return tribonacci_recursief(a, b, c, n-1) + tribonacci_recursief(a, b, c, n-2) + tribonacci_recursief(a, b, c, n-3)
    
