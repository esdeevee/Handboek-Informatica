from random import randint

def aantal_cijfers_recursief(getal):
    if getal == getal % 10:
        # getal heeft één cijfer
        return 1
    else:
        return 1 + aantal_cijfers_recursief(getal // 10)


# suite.yaml voor de TESTed judge
# wis alle gegevens in suite.yaml
file = open("suite.yaml", "w")
file.truncate()
file.close()

with open('suite.yaml', 'a') as file:
    file.write('- tab: "aantal_cijfers_recursief"\n')
    file.write('  testcases:\n')
    for i in range(100):
        aantal_cijfers = randint(0, 100)
        getal = randint(10**aantal_cijfers, 10**(aantal_cijfers+1))
        file.write('    - expression: "aantal_cijfers_recursief(' + str(getal) + ')"\n')
        file.write('      return: ' + str(aantal_cijfers_recursief(getal)) + '\n')
    
