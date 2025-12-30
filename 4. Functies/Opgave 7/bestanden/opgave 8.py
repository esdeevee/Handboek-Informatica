"""
getal_1 = int(input(’Geef een eerste geheel getal: ’))
getal_2 = int(input(’Geef een tweede geheel getal: ’))
if getal_1 == getal_2:
    print(’De getallen zijn gelijk aan elkaar.’)
elif getal_1 > getal_2:
    print(’Het eerste getal is groter dan het tweede getal.’)
else:
    print(’Het eerste getal is kleiner dan het tweede getal.’)
"""

from random import randint

def bmi(m,l):
    BMI = m / l**2
    if(BMI < 18.5):
        uitvoer = str(round(BMI, 1)) + ' ondergewicht'
    elif(18.5 <= BMI < 25):
        uitvoer = str(round(BMI, 1)) + ' gezond gewicht'
    elif(25 <= BMI < 30):
        uitvoer = str(round(BMI, 1)) + ' overgewicht'
    else:
        uitvoer = str(round(BMI, 1)) + ' obesitas'
    return(uitvoer)
    
    

# wis alle gegevens in in.csv
f = open("0.in", "w")
f.truncate()
f.close()
# wis alle gegevens in out.csv
f = open("0.out", "w")
f.truncate()
f.close()

for i in range(100):
  l = randint(150,200) / 100
  BMI = randint(170,320) / 10
  m = round(BMI * l**2, 1)
  with open('0.in', 'a') as f:
    f.write(str(l))
    f.write("\n")
    f.write(str(m))
    f.write("\n")
  with open('0.out', 'a') as g:
    g.write(bmi(m,l))
    g.write("\n")

