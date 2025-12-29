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

        

