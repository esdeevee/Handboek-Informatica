from random import randint, gauss

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

        
# suite.yaml voor de TESTed judge
# wis alle gegevens in suite.yaml
file = open("suite.yaml", "w")
file.truncate()
file.close()

with open('suite.yaml', 'a') as file:
    file.write('- tab: "product_direct"\n')
    file.write('  testcases:\n')
    for i in range(5):
        for j in range(20):
            a = randint(10**(i+1), 10**(i+2))
            b = randint(10**(i+1), 10**(i+2))
            file.write('    - expression: "product_direct(' + str(a) + ', ' + str(b) + ')"\n')
            file.write('      return: ' + str(a*b) + '\n')

    file.write('\n')
    file.write('- tab: "product_iteratief"\n')
    file.write('  testcases:\n')
    for i in range(5):
        for j in range(20):
            a = randint(10**(i+1), 10**(i+2))
            b = randint(10**(i+1), 10**(i+2))
            file.write('    - expression: "product_iteratief(' + str(a) + ', ' + str(b) + ')"\n')
            file.write('      return: ' + str(a*b) + '\n')

    file.write('\n')
    file.write('- tab: "product_recursief"\n')
    file.write('  testcases:\n')
    for i in range(3):
        for j in range(33):
            a = randint(10**(i), 10**(i+1))
            b = randint(10**(i), 10**(i+1))
            file.write('    - expression: "product_recursief(' + str(a) + ', ' + str(b) + ')"\n')
            file.write('      return: ' + str(a*b) + '\n')

