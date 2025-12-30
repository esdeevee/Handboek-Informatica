from math import sqrt

# de functie schuine_zijde() leest de waarde (type float) in van de twee rechthoekszijden in een rechthoekige driehoek
# de uitvoer is de lengte van de schuine zijde (type float)
def schuine_zijde(a, b):
    c = sqrt(a**2 + b**2)
    return(c)

# de functie bereken_sinus() leest de waarde (type float) in van de aanliggende en de overstaande rechthoekszijden in een rechthoekige driehoek
# de uitvoer is de sinus van de hoek (type float)
def bereken_sinus(aanliggende, overstaande):
    schuine = schuine_zijde(aanliggende, overstaande)
    sinus = overstaande / schuine
    return(sinus)

# de functie bereken_cosinus() leest de waarde (type float) in van de aanliggende en de overstaande rechthoekszijden in een rechthoekige driehoek
# de uitvoer is de cosinus van de hoek (type float)
def bereken_cosinus(aanliggende, overstaande):
    schuine = schuine_zijde(aanliggende, overstaande)
    cosinus = aanliggende / schuine
    return(cosinus)


# na de definitie van de drie functies begint hier het hoofdprogramma
a = float(input('Geef de lengte (in cm) van de aanliggende rechthoekszijde: '))
b = float(input('Geef de lengte (in cm) van de overstaande rechthoekszijde: '))
sin_A = bereken_sinus(a, b)
print(sin_A)
cos_A = bereken_cosinus(a, b)
print(cos_A)
