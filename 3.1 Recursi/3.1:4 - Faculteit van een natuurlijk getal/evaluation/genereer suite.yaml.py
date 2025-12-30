from random import randint
from math import factorial

def faculteit_iteratief(n):
    product = 1
    for i in range(1, n+1):
        product = product * i


def faculteit_recursief(n):
    if n == 1:
        return 1
    else:
        return n * faculteit_recursief(n-1)
        
# suite.yaml voor de TESTed judge
# wis alle gegevens in suite.yaml
file = open("suite.yaml", "w")
file.truncate()
file.close()

with open('suite.yaml', 'a') as file:
    file.write('- tab: "faculteit_iteratief"\n')
    file.write('  testcases:\n')
    for i in range(1, 100):
        file.write('    - expression: "faculteit_iteratief(' + str(i) + ')"\n')
        file.write('      return: ' + str(factorial(i)) + '\n')
        
    file.write('\n')
    file.write('- tab: "faculteit_recursief"\n')
    file.write('  testcases:\n')
    for i in range(1, 50):
        file.write('    - expression: "faculteit_recursief(' + str(i) + ')"\n')
        file.write('      return: ' + str(factorial(i)) + '\n')
