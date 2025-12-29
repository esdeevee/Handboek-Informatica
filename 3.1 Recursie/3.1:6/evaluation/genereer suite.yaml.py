from random import randint
from math import factorial

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
        
# suite.yaml voor de TESTed judge
# wis alle gegevens in suite.yaml
file = open("suite.yaml", "w")
file.truncate()
file.close()

with open('suite.yaml', 'a') as file:
    file.write('- tab: "fibonacci_iteratief"\n')
    file.write('  testcases:\n')
    for i in range(1, 100):
        file.write('    - expression: "fibonacci_iteratief(' + str(i) + ')"\n')
        file.write('      return: ' + str(fibonacci_iteratief(i)) + '\n')
        
    file.write('\n')
    file.write('- tab: "fibonacci_recursief"\n')
    file.write('  testcases:\n')
    for i in range(1, 36):
        file.write('    - expression: "fibonacci_recursief(' + str(i) + ')"\n')
        file.write('      return: ' + str(fibonacci_recursief(i)) + '\n')
