from random import randint, gauss

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


        
# suite.yaml voor de TESTed judge
# wis alle gegevens in suite.yaml
file = open("suite.yaml", "w")
file.truncate()
file.close()

with open('suite.yaml', 'a') as file:
    file.write('- tab: "macht_direct"\n')
    file.write('  testcases:\n')
    for i in range(3):
        for j in range(33):
            a = randint(2, 100)
            b = randint(2, 20)
            file.write('    - expression: "macht_direct(' + str(a) + ', ' + str(b) + ')"\n')
            file.write('      return: ' + str(a**b) + '\n')

    file.write('\n')
    file.write('- tab: "macht_iteratief"\n')
    file.write('  testcases:\n')
    for i in range(5):
        for j in range(20):
            a = randint(2, 100)
            b = randint(2, 20)
            file.write('    - expression: "macht_iteratief(' + str(a) + ', ' + str(b) + ')"\n')
            file.write('      return: ' + str(a**b) + '\n')

    file.write('\n')
    file.write('- tab: "macht_recursief"\n')
    file.write('  testcases:\n')
    for i in range(3):
        for j in range(33):
            a = randint(2, 100)
            b = randint(2, 20)
            file.write('    - expression: "macht_recursief(' + str(a) + ', ' + str(b) + ')"\n')
            file.write('      return: ' + str(a**b) + '\n')

