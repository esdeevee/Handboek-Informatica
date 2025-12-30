### Opgave

Marie wilt een bepaald bedrag betalen. Ze heeft een ruime voorraad munten van 1 en 2 en biljetten van 5 euro. Schrijf een functie `aantal_manieren_betalen(bedrag)` die op een recursieve manier berekent en teruggeeft op hoeveel manieren ze `bedrag` kan betalen. 

*Om de wiskundige kant van de zaak niet al te moeilijk te maken, moet je aannemen dat de volgorde waarin Marie betaalt met munten en/of biljetten, van belang is. Als Marie bv. 4 euro wilt betalen, kan ze dat op vijf manieren:*
* 1+1+1+1 = 4
* 1+1+2 = 4
* 1+2+1 = 4 
* 2+1+1 = 4
* 2+2 = 4

*Je zou kunnen zeggen dat er maar drie manieren zijn (1+1+2 = 1+2+1 = 2+1+1 zijn in feite identiek), maar dan wordt het (nog) wat lastiger.* 

*Als je deze gedachte lastig vindt om te aanvaarden, beeld je dan in dat je Opgave 1 opnieuw maakt, waarbij je nu ook de optie hebt om vijf treden in één keer te nemen.*

Test je code in Dodona. Let daarbij op dat je geen hoofdprogramma ingeeft.

### Voorbeeld


**Invoer:**

    > aantal_manieren_betalen(6)

**Uitvoer:**

    15