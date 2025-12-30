# rico() heeft als parameters x1, y1, x2, y2: de x- en y-coordinaten van P en Q. De functie berekent de rico van PQ en stuurt deze waarde terug.
def rico(x1, y1, x2, y2):
    a = (y2 - y1) / (x2 - x1)
    return(a)

# snijpunt_y() heeft als parameters x1, y1, x2, y2: de x- en y-coordinaten van P en Q (floats). De functie berekent de y-coordinaat van het snijpunt van PQ met de y-as (float) en stuurt deze waarde terug.
def snijpunt_y(x1, y1, x2, y2):
    a = rico(x1, y1, x2, y2)
    b = y1 - a * x1
    return(b)

# snijpunt_x() heeft als parameters x1, y1, x2, y2: de x- en y-coordinaten van P en Q (floats). De functie berekent de x-coordinaat van het snijpunt van PQ met de x-as (float) en stuurt deze waarde terug.
def snijpunt_x(x1, y1, x2, y2):
    a = rico(x1, y1, x2, y2)
    b = snijpunt_y(x1, y1, x2, y2)
    nulpunt = -b / a
    return(nulpunt)
