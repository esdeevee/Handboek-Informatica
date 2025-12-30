### Opgave


Kopieer en plak onderstaand programma in een IDE. Voer het programma uit.

```python
from math import sqrt
# definieer de functie schuine_zijde
# deze leest de waarde in van de twee rechthoekszijden en berekent de lengte van de schuine zijde in een rechthoekige driehoek
def schuine_zijde(a, b):
  c = sqrt(a**2 + b**2)
  return(c)

# na de definitie van de functie schuine_zijde begint hier het hoofdprogramma
x = float(input('Geef de lengte (in cm) van de eerste rechthoekszijde: '))
y = float(input('Geef de lengte (in cm) van de tweede rechthoekszijde: '))
z = schuine_zijde(x, y)
print('De lengte van de schuine zijde is gelijk aan', z, 'cm.')
```
