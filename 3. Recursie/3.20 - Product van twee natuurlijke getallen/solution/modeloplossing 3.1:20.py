def product_direct(a, b):
    return a * b

def product_iteratief(a, b):
    product = 0
    for i in range(a):
        product = product + b
    return product

def product_recursief(a, b):
    if b == 1:
        return a
    else:
        return a + product_recursief(a, b - 1)
