### Opgave

Kopieer en plak onderstaande code in je IDE. Voeg aan dit programma een functie `bereken_cosinus()` toe. Deze functie leest (in deze volgorde) de lengte van de aanliggende en de overstaande rechthoekszijde in. De uitvoer van de functie is de cosinus van de hoek $$\mathsf{\hat A}$$. Pas het hoofdprogramma aan zodat de waarde van $$\mathsf{sin \, \hat A}$$ en $$\mathsf{cos \, \hat A}$$ getoond worden, telkens op een nieuwe lijn.

```python
from math import sqrt

# de functie schuine_zijde() leest de waarde (type float) in van de twee rechthoekszijden in een rechthoekige driehoek
# de uitvoer is de lengte van de schuine zijde (type float)
def schuine_zijde(a, b):
    c = sqrt(a**2 + b**2)
    return(c)

# de functie bereken_sinus() leest de waarde (type float) in van de overstaande en de aanliggende rechthoekszijde in een rechthoekige driehoek
# de uitvoer is de sinus van de hoek (type float)
def bereken_sinus(aanliggende, overstaande):
    schuine = schuine_zijde(aanliggende, overstaande)
    sinus = overstaande / schuine
    return(sinus)

# na de definitie van de twee functies begint hier het hoofdprogramma
a = float(input('Geef de lengte (in cm) van de aanliggende rechthoekszijde: '))
b = float(input('Geef de lengte (in cm) van de overstaande rechthoekszijde: '))
sinus = bereken_sinus(a, b)
print(sinus)  
```



### Voorbeeld

**Invoer:**

    Geef de lengte (in cm) van de aanliggende rechthoekszijde: 4
    Geef de lengte (in cm) van de overstaande rechthoekszijde: 3




**Uitvoer:**

    0.6
    0.8
