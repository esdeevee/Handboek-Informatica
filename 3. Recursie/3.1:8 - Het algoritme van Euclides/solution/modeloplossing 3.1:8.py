def Euclides_iteratief(a, b):
    grootste = max(a, b)
    kleinste = min(a, b)
    while True:
        if kleinste == 0:
            # als kleinste gelijk is aan nul, is de ggd gelijk aan grootste
            ggd = grootste
            return ggd
        else:
            # ggd(grootste, kleinste) = ggd(kleinste, rest)
            rest = grootste % kleinste
            grootste = kleinste
            kleinste = rest
    

def Euclides_recursief(a, b):
    grootste = max(a, b)
    kleinste = min(a, b)
    if kleinste == 0:
        # als kleinste gelijk is aan nul, is de ggd gelijk aan grootste
        return grootste
    else:
        rest = a % b
        return Euclides_recursief(b, rest)
