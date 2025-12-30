### Opgave

Schrijf een functie `keer_om(woord)` die op een recursieve manier `woord` omkeert. 


*Hints:* 
* `woord[0]` en `woord[1]` verwijzen respectievelijk naar wat wij het eerste en tweede karakter van `woord` noemen.
* Analoog verwijzen `woord[-1]` en `woord[-2]` respectievelijk naar het laatste en het voorlaatste karakter van `woord`.
* `woord[a:b]` verwijst dan weer naar het deel van `woord` dat begint bij het `a`-de karakter en dat stopt *vlak voor* het `b`-de karakter van `woord`. `'palindroom'[2:5]` geeft dus `'lin'` terug.

Test je code in Dodona. Let daarbij op dat je geen hoofdprogramma ingeeft.

### Voorbeeld


**Invoer:**

    > keer_om('woord')

**Uitvoer:**

    'droow'