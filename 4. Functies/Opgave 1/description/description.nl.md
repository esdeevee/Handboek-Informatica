### Opgave

Kopieer en plak onderstaand programma in een IDE. Voer het programma uit. Geef $$\mathsf{x}$$ de waarde -2. Noteer de uitvoer.

```python
# je gebruikt het functievoorschrift f(x) = 3x+5
# deze functie vraagt een x-waarde x en berekent y=f(x)
def f(x):
  y = 3*x + 5
  return(y)

# na de definitie van de functie f begint hier het hoofdprogramma
x = float(input('Geef een x-waarde: '))
y = f(x)
print(y)
```
