# bereken_BMI() heeft 2 parameters: de lengte (in cm, integer) en de massa (in kg, float) van een persoon. De functie berekent de BMI van deze persoon en stuurt deze terug naar het hoofdprogramma.
# l wordt ingelezen in centimeter, maar de formule eist een lengte in meter
# je moet l dus delen door 100 in de formule om de BMI correct te berekenen
def bereken_BMI(l, m):
    BMI = round(m / (l/100)**2, 1)
    return(BMI)
