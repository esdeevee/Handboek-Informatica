def aantal_cijfers_recursief(getal):
    if getal == getal % 10:
        # getal heeft één cijfer
        return 1
    else:
        return 1 + aantal_cijfers_recursief(getal // 10)
