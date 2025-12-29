from random import randint, gauss

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

"""
# wis alle gegevens in in.csv
file = open("0.in", "w")
file.truncate()
file.close()
# wis alle gegevens in in.csv
file = open("0.out", "w")
file.truncate()
file.close()
# wis alle gegevens in in.csv
file = open("1.in", "w")
file.truncate()
file.close()
# wis alle gegevens in in.csv
file = open("1.out", "w")
file.truncate()
file.close()
# wis alle gegevens in in.csv
file = open("2.in", "w")
file.truncate()
file.close()
# wis alle gegevens in in.csv
file = open("2.out", "w")
file.truncate()
file.close()




# direct
for i in range(5):
    for j in range(20):
        with open('0.in', 'a') as file:
            a = randint(10**(i+1), 10**(i+2))
            b = randint(10**(i+1), 10**(i+2))
            file.write('>>> som_direct(' + str(a) + ', ' + str(b) +')')
            file.write('\n')

            file.write("'" + str(som_direct(a, b)) + "'")
            file.write('\n')
            #file.write('\n')

# iteratief
for i in range(5):
    for j in range(20):
        with open('1.in', 'a') as file:
            a = randint(10**(i+1), 10**(i+2))
            b = randint(10**(i+1), 10**(i+2))
            file.write('>>> som_iteratief(' + str(a) + ', ' + str(b) +')')
            file.write('\n')

            file.write("'" + str(som_direct(a, b)) + "'")
            file.write('\n')
            #file.write('\n')

# recursief
for i in range(5):
    for j in range(20):
        with open('2.in', 'a') as file:
            a = randint(10**(i+1), 10**(i+2))
            b = randint(10**(i+1), 10**(i+2))
            file.write('>>> som_recursief(' + str(a) + ', ' + str(b) +')')
            file.write('\n')

            file.write("'" + str(som_direct(a, b)) + "'")
            file.write('\n')
            #file.write('\n')
"""
        
# suite.yaml voor de TESTed judge
# wis alle gegevens in suite.yaml
file = open("suite.yaml", "w")
file.truncate()
file.close()

with open('suite.yaml', 'a') as file:
    file.write('- tab: "som_direct"\n')
    file.write('  testcases:\n')
    for i in range(5):
        for j in range(20):
            a = randint(10**(i+1), 10**(i+2))
            b = randint(10**(i+1), 10**(i+2))
            file.write('    - expression: "som_direct(' + str(a) + ', ' + str(b) + ')"\n')
            file.write('      return: ' + str(som_direct(a, b)) + '\n')

    file.write('\n')
    file.write('- tab: "som_iteratief"\n')
    file.write('  testcases:\n')
    for i in range(5):
        for j in range(20):
            a = randint(10**(i+1), 10**(i+2))
            b = randint(10**(i+1), 10**(i+2))
            file.write('    - expression: "som_iteratief(' + str(a) + ', ' + str(b) + ')"\n')
            file.write('      return: ' + str(som_direct(a, b)) + '\n')

    file.write('\n')
    file.write('- tab: "som_recursief"\n')
    file.write('  testcases:\n')
    for i in range(4):
        for j in range(25):
            a = randint(10**(i), 10**(i+1))
            b = randint(10**(i), 10**(i+1))
            file.write('    - expression: "som_recursief(' + str(a) + ', ' + str(b) + ')"\n')
            file.write('      return: ' + str(som_direct(a, b)) + '\n')

