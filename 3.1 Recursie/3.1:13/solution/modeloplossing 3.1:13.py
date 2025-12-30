def keer_om(woord):
    if len(woord) == 1:
        # een woord van 1 letter omkeren geeft gewoon dezelfde letter
        return woord
    else:
        # woord heeft minstens 2 letters
        # we selecteren de laatste letter,
        # en plakken hier het omgekeerde van de rest van woord aan vast
        return woord[-1] + keer_om(woord[:-1])
