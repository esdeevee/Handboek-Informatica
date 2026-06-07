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
