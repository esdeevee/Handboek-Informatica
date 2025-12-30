# cm_naar_ft() heeft 1 parameter: de lengte van een persoon in cm (float). Het berekent het aantal foot dat hier in past (integer) en stuurt deze waarde terug.
def cm_naar_ft(l):
    # foot moet een natuurlijk getal zijn, dus gebruik de functie round()
    foot = round(l // 30.48)
    return(foot)

# cm_naar_in() heeft 1 parameter: de lengte van een persoon in cm (float). Het berekent het aantal inch dat nog in de lengte past (integer) nadat het aantal foot er van afgetrokken is. Deze waarde wordt afgerond op 0,1 inch en teruggestuurd.
def cm_naar_in(l):
    foot = cm_naar_ft(l)
    inch = round((l % 30.48) / 2.54, 1)
    return(inch)
