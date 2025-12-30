### Inleiding

De oud-Griekse wiskundige Euclides heeft rond 300 v.C. een algoritme bedacht om de grootste gemene deler (ggd) van twee getallen te berekenen. Het algoritme steunt op het herhaaldelijk toepassen van de eigenschap:

> De grootste gemene deler van $$\mathsf{grootste\_getal}$$ en $$\mathsf{kleinste\_getal}$$ is gelijk aan de grootste gemene deler van $$\mathsf{kleinste\_getal}$$ en de rest bij deling van $$\mathsf{grootste\_getal}$$ door $$\mathsf{kleinste\_getal}$$.

### Voorbeeld
* ggd(752, 372) = ggd(372, 8) want 752 = 2 $$\cdot$$ 372 + 8
* ggd(372, 8) = ggd(8, 4) want 372 = 46 $$\cdot$$ 8 + 4
* ggd(8, 4) = ggd(4, 0) want 8 = 2 \cdot 4 + 0$$
* ggd(4, 0) = 4 want elk getal is een deler van nul
* $$Rightarrow$$ ggd(752, 372) = 4

### Opgave

* Schrijf een functie `Euclides_iteratief(a, b)` die op een iteratieve manier de grootste gemene deler van $$a$$ en $$b$$ berekent en toont. 
* Schrijf een functie `Euclides_recursief(a, b)` die op een recursieve manier de grootste gemene deler van $$a$$ en $$b$$ berekent en toont. 

Test je code in Dodona. Let daarbij op dat je geen hoofdprogramma ingeeft.

### Voorbeeld


**Invoer:**

    > Euclides_iteratief(10, 64)

**Uitvoer:**

    2


**Invoer:**

    > Euclides_recursief(52, 91)

**Uitvoer:**

    13
