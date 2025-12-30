def faculteit_iteratief(n):
    product = 1
    for i in range(1, n+1):
        product = product * i
    return product


def faculteit_recursief(n):
    if n == 1:
        return 1
    else:
        return n * faculteit_recursief(n-1)
