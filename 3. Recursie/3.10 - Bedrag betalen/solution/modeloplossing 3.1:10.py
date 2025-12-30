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
