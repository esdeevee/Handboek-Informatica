### Inleiding

De rij van Fibonacci is wellicht het typevoorbeeld van een wiskundige rij die heel gemakkelijk recursief kan worden gedefinieerd. Als we het $$n$$-de getal van Fibonacci noteren als $$F_n$$, kan je de rij van Fibonacci formeel definiëren als volgt:
* de eerste en de tweede term van de rij zijn gelijk aan 1:

$$
F_1 = F_2 = 1.
$$

* elke volgende term is gelijk aan de som van de twee voorgaande termen: 

$$
F_n = F_{n-1} + F_{n-2} \hspace{1cm} (n \geq 3)
$$

De rij van Fibonacci bestaat dus uit de getallen 1, 1, 2, 3, 5, 8, 13, 21, … 

### Opgave

* Schrijf een functie `fibonacci_iteratief(n)` die op een iteratieve manier $$F_n$$ berekent en teruggeeft. 
* Schrijf een functie `fibonacci_recursief(n)` die op een recursieve manier $$F_n$$ berekent en teruggeeft. 

Test je code in Dodona. Let daarbij op dat je geen hoofdprogramma ingeeft.

### Voorbeeld

**Invoer:**

    > fibonacci_iteratief(6)

**Uitvoer:**

    8


**Invoer:**

    > fibonacci_recursief(8) 

**Uitvoer:**

    21
