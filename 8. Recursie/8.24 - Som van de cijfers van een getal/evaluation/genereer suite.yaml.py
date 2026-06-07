from random import randint

def som_van_de_cijfers_recursief(getal):
    # basisgeval: het getal bestaat uit één cijfer
    if getal < 10:
        return getal

    # recursiestap
    # het getal bestaat uit minstens twee cijfers
    else:
        # we lossen de zaak op via strings
        getal = str(getal)

        # het eerste cijfer is het eerste karakter van de string getal
        eerste_cijfer = getal[0]
        # zet terug om naar een integer
        eerste_cijfer = int(eerste_cijfer)

        # bereken de rest van het getal
        rest = getal[1:]
        rest = int(rest)

        # bereken de som op een recursieve manier
        return eerste_cijfer + som_van_de_cijfers_recursief(rest)



# suite.yaml voor de TESTed judge
# wis alle gegevens in suite.yaml
file = open("suite.yaml", "w")
file.truncate()
file.close()

with open('suite.yaml', 'a') as file:
    file.write('- tab: "aantal_cijfers_recursief"\n')
    file.write('  testcases:\n')
    for i in range(10):
        for j in range(10):
            aantal_cijfers = randint(0, (i+1) ** 2)
            getal = randint(10**aantal_cijfers, 10**(aantal_cijfers+1))
            file.write('    - expression: "som_van_de_cijfers_recursief(' + str(getal) + ')"\n')
            file.write('      return: ' + str(som_van_de_cijfers_recursief(getal)) + '\n')
    
