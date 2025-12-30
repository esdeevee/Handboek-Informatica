from random import randint

def keer_om(woord):
    if len(woord) == 1:
        # een woord van 1 letter omkeren geeft gewoon dezelfde letter
        return woord
    else:
        # woord heeft minstens 2 letters
        # we selecteren de laatste letter,
        # en plakken hier het omgekeerde van de rest van woord aan vast
        return woord[-1] + keer_om(woord[:-1])

# Een ruime, gevarieerde set Nederlandse woorden (algemeen bruikbaar)
WOORDEN = [
    "huis","boom","fiets","school","leerling","tafel","stoel","raam","deur","straat","plein",
    "water","vuur","aarde","lucht","zon","maan","ster","computer","programma","code","functie",
    "variabele","docent","student","boek","schrift","pen","potlood","gum","bord","krijt","kaart",
    "wereld","land","stad","dorp","winkel","bakker","slager","apotheek","ziekenhuis","dokter",
    "verpleegkundige","trein","tram","bus","metro","auto","vliegtuig","schip","haven","brug","tunnel",
    "park","tuin","bloem","plant","gras","boomgaard","bos","dier","kat","hond","vis","vogel","konijn",
    "koe","paard","schaap","geit","kip","ei","melk","brood","kaas","boter","fruit","appel","peer",
    "banaan","kers","druif","perzik","pruim","aardbei","citroen","sinaasappel","mandarijn","groente",
    "tomaat","komkommer","paprika","wortel","ui","knoflook","prei","selder","kool","bloemkool","spinazie",
    "erwt","boon","linze","rijst","pasta","saus","soep","suiker","zout","peper","olie","azijn","kruiden",
    "kaneel","vanille","chocolade","koek","taart","toetje","yoghurt","koffie","thee","limonade","bier",
    "wijn","whisky","sap","sport","voetbal","basketbal","tennis","zwemmen","lopen","fietsen","schaatsen",
    "turnen","muziek","lied","zang","gitaar","piano","viool","drum","orkest","concert","film","serie",
    "theater","museum","kunst","schilderij","beeld","foto","camera","telefoon","tablet","laptop","internet",
    "website","server","netwerk","wachtwoord","beveiliging","privacy","gegevens","opslag","bestand","map",
    "folder","tekst","zin","woord","letter","taal","Nederlands","Frans","Engels","Duits","Spaans","Italiaans",
    "Portugees","Japans","Chinees","Arabisch","Hebreeuws","les","klas","examen","toets","punt","cijfer","rapport",
    "schooljaar","vakantie","zomer","winter","herfst","lente","maandag","dinsdag","woensdag","donderdag","vrijdag",
    "zaterdag","zondag","uur","minuut","seconde","dag","week","maand","jaar","gisteren","vandaag","morgen",
    "ochtend","middag","avond","nacht","vriendschap","familie","ouder","kind","zoon","dochter","broer","zus",
    "oom","tante","neef","nicht","opa","oma","gezin","huiswerk","project","taak","plan","idee","vraag","antwoord",
    "probleem","oplossing","voorbeeld","regel","wet","recht","plichten","verantwoordelijkheid","afspraak",
    "vergadering","brief","mail","bericht","spraak","geluid","ruis","stilte","licht","donker","kleuren","rood",
    "blauw","groen","geel","oranje","paars","wit","zwart","grijs","bruin","goud","zilver","vorm","cirkel","vierkant",
    "driehoek","lijn","punt","grafiek","tabel","getal","som","optellen","aftrekken","vermenigvuldigen","delen",
    "gemiddelde","mediaan","modus","kans","statistiek","algebra","meetkunde","rekening","budget","bank","geld",
    "euro","betaling","factuur","bon","prijs","korting","markt","economie","wetenschap","natuur","chemie","fysica",
    "biologie","astronomie","ruimte","planeet","galaxie","universum"
]




# suite.yaml voor de TESTed judge
# wis alle gegevens in suite.yaml
file = open("suite.yaml", "w")
file.truncate()
file.close()

with open('suite.yaml', 'a') as file:
    file.write('- tab: "keer_om"\n')
    file.write('  testcases:\n')
    for i in range(100):
        woord = "'" + WOORDEN[i] + "'"
        file.write('    - expression: "keer_om(' + woord + ')"\n')
        file.write('      return: ' + str(keer_om(woord)) + '\n')
    
                
  
