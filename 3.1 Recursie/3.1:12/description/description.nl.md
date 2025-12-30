### Inleiding

Een palindroom is een woord dat hetzelfde wordt gelezen van voor naar achter als van achter naar voor. Voorbeelden zijn *pop*, *raar* of *lepel*. 


### Opgave

Schrijf een functie `is_palindroom(woord)` die op een recursieve manier nagaat of `woord` een palindroom is. 

*Hints:* 
* `woord[0]` en `woord[1]` verwijzen respectievelijk naar wat wij het eerste en tweede karakter van `woord` noemen.
* Analoog verwijzen `woord[-1]` en `woord[-2]` respectievelijk naar het laatste en het voorlaatste karakter van `woord`.
* `woord[a:b]` verwijst dan weer naar het deel van `woord` dat begint bij het `a`-de karakter en dat stopt *vlak voor* het `b`-de karakter van `woord`. `palindroom[2:5]` geeft dus `lin` terug.

Test je code in Dodona. Let daarbij op dat je geen hoofdprogramma ingeeft.

### Voorbeeld


**Invoer:**

    > is_palindroom('palindroom')

**Uitvoer:**

    False


**Invoer:**

    > is_palindroom('legovogel')

**Uitvoer:**

    True
