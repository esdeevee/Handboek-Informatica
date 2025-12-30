### Inleiding

We beschouwen de rij van Tribonacci, een variant op de rij van Fibonacci. Deze rij heeft drie variabelen $$a$$, $$b$$ en $$c$$. Als we het $$n$$-de getal van Tribonacci noteren als $$T_n$$, kan je deze rij formeel definiëren als volgt:
* $$T_1 = a$$, $$T_2 = b$$, $$T_3 = c$$.
* $$T_n = T_{n-1} + T_{n-2} + T_{n-3}  (n \geq 4)$$.
 

### Opgave

Schrijf een functie `tribonacci_recursief(a,b,c,n)` die op een recursieve manier $$T_n$$ berekent en teruggeeft. 

Test je code in Dodona. Let daarbij op dat je geen hoofdprogramma ingeeft.

### Voorbeeld


**Invoer:**

    > tribonacci_recursief(2, 3, 4, 5) 

**Uitvoer:**

    21
