# F_naar_C() heeft als parameter een temperatuur in graden F (float). De functie zet deze temperatuur om naar graden C (float) en stuurt de gevonden waarde terug.

def F_naar_C(F):
    C = round((F - 32) * ( 5 / 9), 1)
    return(C)
