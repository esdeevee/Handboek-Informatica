from random import randint, gauss

def aantal_manieren_trap(n):
    # n is een natuurlijk getal
    if n <= 1:
	    # voor een trap met 0 of 1 trede is het probleem al opgelost
	    # er is maar 1 manier om een trap met 0 of 1 trede te beklimmen
	    return 1
    else:
	    # het aantal trappen is minstens 2
	    # we noteren het patroon dat we ingezien hadden
	    return aantal_manieren_trap(n - 1) + aantal_manieren_trap(n - 2)

        
# suite.yaml voor de TESTed judge
# wis alle gegevens in suite.yaml
file = open("suite.yaml", "w")
file.truncate()
file.close()

with open('suite.yaml', 'a') as file:
    file.write('- tab: "aantal_manieren_trap"\n')
    file.write('  testcases:\n')
    for i in range(5):
        n = randint(5, 20)
        file.write('    - expression: "aantal_manieren_trap(' + str(n) + ')"\n')
        file.write('      return: ' + str(aantal_manieren_trap(n)) + '\n')

    
