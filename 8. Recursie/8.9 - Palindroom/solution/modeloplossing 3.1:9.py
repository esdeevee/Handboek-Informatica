def is_palindroom(woord):
    # 1. basisstap
    # een woord van 1 letter is altijd een palindroom
    if len(woord) == 1:
        return True
    # een woord van 2 letters is een palindroom als beide letters gelijk zijn, en anders niet
    if len(woord) == 2:
        if woord[0] == woord[1]:
            return True
        else:
            return False
    # 2. recursiestap
    else:    
        # we hebben een woord van minstens drie letters
        # we kunnen niet in één keer uitspraak doen over het al dan niet palindroom zijn van het woord
        # als de eerste en de laatste letter verschillen, is het woord zeker geen palindroom
        # als woord = 'mooi', kunnen we al zeker besluiten dat het geen palindroom is
        # want 'm' != 'i'
        # het feit dat de twee middenste letters gelijk zijn, verandert daar niets aan
        if woord[0] != woord[-1]:
            return False
        # als de eerste en de laatste letter van het woord gelijk zijn, is er kans dat het woord een palindroom is
        # dit is bv. het geval als woord = 'taart'
        # de eerste en de laatste letter zijn gelijk
        # alles hangt af van de rest van het woord: 'aar', wat geen palindroom is
        # ander voorbeeld: woord = 'lepel'
        # de eerste en de laatste letter zijn gelijk
        # we gaan verder met 'epe', wat wel een palindroom zal blijken te zijn
        # we roepen de functie dus op met een beperkte versie van het woord
        # we laten de eerste en de laatste letter weg
        else:
            return is_palindroom(woord[1:-1])
    
