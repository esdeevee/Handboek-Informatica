def is_palindroom(woord):
    if len(woord) == 1:
        # basisstap 1: een woord van 1 letter is altijd een palindroom
        return True
    if len(woord) == 2:
        # basisstap 2: een woord van 2 letters
        if woord[0] == woord[1]:
            # een woord van 2 gelijke letters is een palindroom
            return True
        else:
            # een woord van 2 verschillende letters is geen palindroom
            return False
    if woord[0] != woord[-1]:
        # een woord waarvan de eerste letter verschilt van de laatste, is geen palindroom
        return False
    else:
        # de eerste letter van woord is gelijk aan de laatste
        # dat houdt de mogelijkheid open voor een palindroom
        # we laten de eerste en de laatste letter van woord weg
        woord = woord[1:-1]
        # we gaan recursief verder met deze gestripte versie van woord
        return is_palindroom(woord)
