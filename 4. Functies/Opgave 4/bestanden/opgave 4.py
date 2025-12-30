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

def vergelijk(getal_1,getal_2):
    if getal_1 == getal_2:
        uitvoer = 'De getallen zijn gelijk aan elkaar.'
    elif getal_1 > getal_2:
        uitvoer = 'Het eerste getal is groter dan het tweede getal.'
    else:
        uitvoer = 'Het eerste getal is kleiner dan het tweede getal.'
    return(uitvoer)

# wis alle gegevens in in.csv
f = open("0.in", "w")
f.truncate()
f.close()
# wis alle gegevens in out.csv
f = open("0.out", "w")
f.truncate()
f.close()

for i in range(20):
  getal_1 = randint(0,10)
  gelijk = randint(1,3)
  if gelijk == 1:
     getal_2 = getal_1
  else:
     getal_2 = randint(0,10)
  with open('0.in', 'a') as f:
    f.write(str(getal_1))
    f.write("\n")
    f.write(str(getal_2))
    f.write("\n")
  with open('0.out', 'a') as g:
    g.write(vergelijk(getal_1,getal_2))
    g.write("\n")

for i in range(20):
  getal_1 = randint(-10,10)
  gelijk = randint(1,3)
  if gelijk == 1:
     getal_2 = getal_1
  else:
     getal_2 = randint(-10,10)
  with open('0.in', 'a') as f:
    f.write(str(getal_1))
    f.write("\n")
    f.write(str(getal_2))
    f.write("\n")
  with open('0.out', 'a') as g:
    g.write(vergelijk(getal_1,getal_2))
    g.write("\n")

for i in range(20):
  getal_1 = randint(-100,100)
  gelijk = randint(1,3)
  if gelijk == 1:
     getal_2 = getal_1
  else:
     getal_2 = randint(-100,100)
  with open('0.in', 'a') as f:
    f.write(str(getal_1))
    f.write("\n")
    f.write(str(getal_2))
    f.write("\n")
  with open('0.out', 'a') as g:
    g.write(vergelijk(getal_1,getal_2))
    g.write("\n")

for i in range(20):
  getal_1 = randint(-1000,1000)
  gelijk = randint(1,3)
  if gelijk == 1:
     getal_2 = getal_1
  else:
     getal_2 = randint(-1000,1000)
  with open('0.in', 'a') as f:
    f.write(str(getal_1))
    f.write("\n")
    f.write(str(getal_2))
    f.write("\n")
  with open('0.out', 'a') as g:
    g.write(vergelijk(getal_1,getal_2))
    g.write("\n")

for i in range(20):
  getal_1 = randint(-10000,10000)
  gelijk = randint(1,3)
  if gelijk == 1:
     getal_2 = getal_1
  else:
     getal_2 = randint(-10000,10000)
  with open('0.in', 'a') as f:
    f.write(str(getal_1))
    f.write("\n")
    f.write(str(getal_2))
    f.write("\n")
  with open('0.out', 'a') as g:
    g.write(vergelijk(getal_1,getal_2))
    g.write("\n")
