import dutch_words
words = dutch_words.get_ranked()
from random import randint

def aantal_medeklinkers(woord):
    # initialiseer twee numerieke variabelen:
    aantal_klinkers = 0
    aantal_medeklinkers = 0
    # herhaal voor elke letter in het woord
    for letter in woord:
        # controleer of letter een klinker is
        if(letter == "a" or letter == "e" or letter == "i" or letter == "o" or letter == "u"):
            # zo ja, verhoog dan de waarde van aantal_klinkers met 1
            aantal_klinkers = aantal_klinkers + 1
        # letter is geen klinker, dus het is een medeklinker
        else:
            # verhoog de waarde van aantal_medeklinkers met 1
            aantal_medeklinkers = aantal_medeklinkers + 1
    # print de uitvoer
    uitvoer = woord + " heeft " + str(aantal_klinkers) + " klinkers en " + str(aantal_medeklinkers) + " medeklinkers"
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
  n = randint(1,len(words))
  woord = words[n].lower()
  with open('0.in', 'a') as f:
    f.write(woord)
    f.write("\n")
  with open('0.out', 'a') as g:
    g.write(aantal_medeklinkers(woord))
    g.write("\n")
