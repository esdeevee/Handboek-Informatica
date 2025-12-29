from random import randint
from math import factorial




def aantal_manieren_betalen_AI(bedrag: int) -> int:
    if bedrag < 0:
        return 0
    if bedrag == 0:
        return 1
    return (aantal_manieren_betalen_AI(bedrag - 1) +
            aantal_manieren_betalen_AI(bedrag - 2) +
            aantal_manieren_betalen_AI(bedrag - 5))


def aantal_manieren_betalen(bedrag):
    if bedrag == 1:
        return 1
    if bedrag == 2:
        return 2
    if bedrag == 3:
        return aantal_manieren_betalen(1) + aantal_manieren_betalen(2)
    if bedrag == 4:
        return aantal_manieren_betalen(2) + aantal_manieren_betalen(3)
    if bedrag == 5:
        return aantal_manieren_betalen(3) + aantal_manieren_betalen(4) + 1
    else:
        return aantal_manieren_betalen(bedrag-1) + aantal_manieren_betalen(bedrag-2) + aantal_manieren_betalen(bedrag-5)

  
# suite.yaml voor de TESTed judge
# wis alle gegevens in suite.yaml
file = open("suite.yaml", "w")
file.truncate()
file.close()

with open('suite.yaml', 'a') as file:
    file.write('- tab: "aantal_manieren_betalen"\n')
    file.write('  testcases:\n')
    for i in range(1, 33):
        file.write('    - expression: "aantal_manieren_betalen(' + str(i) + ')"\n')
        file.write('      return: ' + str(aantal_manieren_betalen(i)) + '\n')
    
