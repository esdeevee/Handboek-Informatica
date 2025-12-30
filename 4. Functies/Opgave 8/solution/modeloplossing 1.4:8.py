# importeer de vierkantswortelfunctie en de constante pi
from math import pi, sqrt

# de functie A_naar_r() heeft als parameter de oppervlakte van een cirkel (in cm2) en berekent de straal van de cirkel (in cm), afgerond op 1 mm. Beide waarden zijn floats.
def A_naar_r(A):
    r = round(sqrt(A/pi), 1)
    return(r)
