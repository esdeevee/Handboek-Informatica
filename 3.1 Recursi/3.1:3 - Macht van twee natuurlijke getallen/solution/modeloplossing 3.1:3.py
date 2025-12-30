def macht_direct(a, b):
    return a ** b

def macht_iteratief(a, b):
    product = 1
    for i in range(b):
        product = product * a
    return product

def macht_recursief(a, b):
    if b == 1:
        return a
    else:
        return a * macht_recursief(a, b - 1)
