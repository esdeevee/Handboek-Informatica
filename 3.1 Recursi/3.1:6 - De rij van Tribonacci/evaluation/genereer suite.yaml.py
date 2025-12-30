from random import randint
from math import factorial


def tribonacci_recursief_AI(a, b, c, n):
    """
    Bereken T_n voor de Tribonacci-rij met startwaarden a, b, c.
    Definities:
      T1 = a, T2 = b, T3 = c
      Tn = T_{n-1} + T_{n-2} + T_{n-3}  (voor n >= 4)
    """

    if n <= 0:
        raise ValueError("n moet een positief geheel getal zijn (n >= 1).")
    if n == 1:
        return a
    if n == 2:
        return b
    if n == 3:
        return c

    # Recursieve stap
    return (tribonacci_recursief_AI(a, b, c, n - 1) +
            tribonacci_recursief_AI(a, b, c, n - 2) +
            tribonacci_recursief_AI(a, b, c, n - 3))


def tribonacci_recursief(a, b, c, n):
    if n == 1:
        return a
    if n == 2:
        return b
    if n == 3:
        return c
    else:
        return tribonacci_recursief(a, b, c, n-1) + tribonacci_recursief(a, b, c, n-2) + tribonacci_recursief(a, b, c, n-3)
    
   
# suite.yaml voor de TESTed judge
# wis alle gegevens in suite.yaml
file = open("suite.yaml", "w")
file.truncate()
file.close()

with open('suite.yaml', 'a') as file:
    file.write('- tab: "tribonacci_recursief"\n')
    file.write('  testcases:\n')
    for i in range(1, 100):
        a = randint(1, 100)
        b = randint(1, 100)
        c = randint(1, 100)
        n = randint(1, 25)
        file.write('    - expression: "tribonacci_recursief(' + str(a) + ', ' + str(b) + ', ' + str(c) + ', ' + str(n) + ')"\n')
        file.write('      return: ' + str(tribonacci_recursief(a, b, c, n)) + '\n')
     
