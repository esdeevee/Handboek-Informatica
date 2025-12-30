def som_direct(a, b):
    return a + b

def som_iteratief(a, b):
    for i in range(a):
        b = b + 1
    return b

def som_recursief(a, b):
    if b == 0:
        return a
    else:
        return som_recursief(a + 1, b - 1)
