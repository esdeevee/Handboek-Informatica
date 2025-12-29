### Opgave

Je wilt een trap met `n` treden beklimmen. Je kunt telkens 1 of 2 treden tegelijk nemen. Hoeveel verschillende manieren zijn er om de trap te beklimmen?

We proberen deze opgave op te lossen voor kleine waarden van `n`:
* Voor `n` = 0: 
* Voor `n` = 1: 
* Voor `n` = 2: 
* Voor `n` = 3: 
* Voor `n` = 4: 

Door te redeneren met kleine waarden van `n` en deze stelselmatig groter te laten worden, zie je dat er een bepaald patroon verscholen zit in de oplossing. Meer bepaald vind je voor een trap met `n` treden het aantal manieren als de som van het aantal manieren om een trap met `n-1` te beklimmen, en het aantal manieren om een trap met `n-2` treden te beklimmen. 

Stel dat we een functie `aantal_manieren(n)` zouden hebben die het antwoord geeft op deze opgave, dan zouden we dus kunnen schrijven dat 

`aantal_manieren(n) = aantal_manieren(n-1) + aantal_manieren(n-2)`.

De oplossing van ons probleem is dus de som van de oplossingen van twee eenvoudigere problemen. Je zou dan kunnen denken dat we het probleem alleen maar verschuiven, want als we `aantal_manieren(n)` niet kennen, hoe zouden we `aantal_manieren(n-1)` en `aantal_manieren(n-2)` dan wel kunnen berekenen?

Om deze vraag te beantwoorden, moet je je realiseren dat `n` een natuurlijk getal is. Er bestaat geen grootste natuurlijk getal, maar de verzameling $$\mathbb{N}$$ is wel naar onder begrensd. 0 en 1 zijn de twee kleinste natuurlijke getallen. 

Dat alles maakt dat we de functie `aantal_manieren(n)` op een subtiele manier kunnen implementeren:

```python
def aantal_manieren(n):
    # n is een natuurlijk getal
    if n <= 1:
	# voor een trap met 0 of 1 trede is het probleem al opgelost
	# er is maar 1 manier om een trap met 0 of 1 trede te beklimmen
	return 1
    else:
	# het aantal trappen is minstens 2
	# we noteren het patroon dat we ingezien hadden
	return aantal_manieren(n - 1) + aantal_manieren(n - 2)

print(aantal_manieren(0))

print(aantal_manieren(0))
```

Voer het programma uit in de Sandbox. Pas daarna de code aan en noteer de uitvoer voor volgende waarden van `n`:
* `aantal_manieren(0)` = 
* `aantal_manieren(1)` = 
* `aantal_manieren(2)` = 
* `aantal_manieren(3)` = 
* `aantal_manieren(4)` = 
* `aantal_manieren(10)` = 
* `aantal_manieren(20)` = 
* `aantal_manieren(35)` = 

Je merkt dat de benodigde rekentijd snel toeneemt met `n`. Om `aantal_manieren(35)` te berekenen, heeft Dodona misschien wel een halve minuut of meer nodig. Mogelijk krijg je de uitvoer zelfs nooit te zien omdat de uitvoering van je programma automatisch beëindigd wordt na een bepaalde tijd.
