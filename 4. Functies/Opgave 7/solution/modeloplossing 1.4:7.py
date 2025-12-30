# x_middelpunt() heeft als invoer de x- en y-coordinaten (floats) van de punten P en Q. De functie stuurt de x-coordinaat van het middelpunt (float) terug.
def x_middelpunt(x1, y1, x2, y2):
    x_M = (x1 + x2) / 2
    return(x_M)

# y_middelpunt() heeft als invoer de x- en y-coordinaten (floats) van de punten P en Q. De functie stuurt de y-coordinaat van het middelpunt (float) terug.
def y_middelpunt(x1, y1, x2, y2):
    y_M = (y1 + y2) / 2
    return(y_M)

# lengte_PQ() heeft als invoer de x- en y-coordinaten (floats) van de punten P en Q. De functie stuurt de lengte van het lijnstuk PQ (float) terug.
def lengte_PQ(x1, y1, x2, y2):
    from math import sqrt
    l = sqrt((x2-x1)**2 + (y2-y1)**2)
    return(l)
