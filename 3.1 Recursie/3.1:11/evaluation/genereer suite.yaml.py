from random import randint

def Euclides_iteratief(a, b):
    grootste = max(a, b)
    kleinste = min(a, b)
    while True:
        if kleinste == 0:
            # als kleinste gelijk is aan nul, is de ggd gelijk aan grootste
            ggd = grootste
            return ggd
        else:
            # ggd(grootste, kleinste) = ggd(kleinste, rest)
            rest = grootste % kleinste
            grootste = kleinste
            kleinste = rest
    

def Euclides_recursief(a, b):
    grootste = max(a, b)
    kleinste = min(a, b)
    if kleinste == 0:
        # als kleinste gelijk is aan nul, is de ggd gelijk aan grootste
        return grootste
    else:
        rest = a % b
        return Euclides_recursief(b, rest)
    

# suite.yaml voor de TESTed judge
# wis alle gegevens in suite.yaml
file = open("suite.yaml", "w")
file.truncate()
file.close()

with open('suite.yaml', 'a') as file:
    file.write('- tab: "Euclides_iteratief"\n')
    file.write('  testcases:\n')
    for i in range(4):
        a = randint(10**10, 10**11)
        b = randint(10**10, 10**11)
        file.write('    - expression: "Euclides_iteratief(' + str(a) + ', ' + str(b) + ')"\n')
        file.write('      return: ' + str(Euclides_iteratief(a, b)) + '\n')
    for i in range(24):
        for j in range(4):
            while True:
                a = randint(10**i, 10**(i+1))
                b = randint(10**i, 10**(i+1))
                ggd = Euclides_iteratief(a, b)
                if ggd != 1:
                    file.write('    - expression: "Euclides_iteratief(' + str(a) + ', ' + str(b) + ')"\n')
                    file.write('      return: ' + str(Euclides_iteratief(a, b)) + '\n')
                    break
                
        
    file.write('- tab: "Euclides_recursief"\n')
    file.write('  testcases:\n')
    for i in range(4):
        a = randint(10**10, 10**11)
        b = randint(10**10, 10**11)
        file.write('    - expression: "Euclides_recursief(' + str(a) + ', ' + str(b) + ')"\n')
        file.write('      return: ' + str(Euclides_recursief(a, b)) + '\n')
    for i in range(24):
        for j in range(4):
            while True:
                a = randint(10**i, 10**(i+1))
                b = randint(10**i, 10**(i+1))
                ggd = Euclides_recursief(a, b)
                if ggd != 1:
                    file.write('    - expression: "Euclides_recursief(' + str(a) + ', ' + str(b) + ')"\n')
                    file.write('      return: ' + str(Euclides_recursief(a, b)) + '\n')
                    break
