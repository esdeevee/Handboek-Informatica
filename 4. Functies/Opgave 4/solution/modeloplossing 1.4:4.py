# importeer de constante pi
from math import pi

# hier komt de definitie van een functie die de straal van een cirkel (in cm) inleest en de oppervlakte van de cirkel (in cm2, afgerond op 1 mm2) terugstuurt naar het hoofdprogramma
def oppervlakte_cirkel(r):
  A = pi * r**2
  return(round(A, 2))

# hier begint het hoofdprogramma
# vraag aan de gebruiker wat de straal is van de cirkel
straal = float(input('Geef de straal van de cirkel: '))
# roep de functie oppervlakte_cirkel() op en toon het resultaat
print(oppervlakte_cirkel(straal))
