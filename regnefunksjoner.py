"""
Dette programmet inneholder regnefunksjoner. 
"""
def addisjon(adder1, adder2):
    """
    Funksjon som tar inn to tall, og returnerer summen av disse.
    """
    return adder1 + adder2

print(addisjon(1, 4))

def subtraksjon(minuend, subtrahend):
    """
    Funksjon som tar inn to tall, og returnerer differensen av disse. 
    """
    return minuend - subtrahend

assert subtraksjon(10, 5) == 5, "Naa ble det feil i subtraksjonen"
assert subtraksjon(5, -10) == 15, "Naa ble det feil i subtraksjonen"
assert subtraksjon(-2, -8) == 6, "Naa ble det feil i subtraksjonen"

def divisjon(dividend, divisor):
    """
    Funksjon som tar inn to tall, og returnerer kvotienten av disse. 
    """
    return dividend/divisor

assert divisjon(10, 5) == 2, "Naa ble det feil i divisjonen"
assert divisjon(-15, 5) == -3,  "Naa ble det feil i divisjonen"
assert divisjon(-8, -2) == 4, "Naa ble det feil i divisjonen"

def tommerTilCm(antallTommer):
    """
    Funksjon som gjor om fra tommer til cm, og returnerer denne verdien. 
    """
    assert antallTommer > 0, "Antall tommer er mindre eller lik 0."
    return antallTommer * 2.54

print(tommerTilCm(54))

def skrivBeregninger():
    """
    Funksjon som ber bruker om to tall, og printer resultatet av addisjon, subtraksjon og divisjon
    med disse som parametre. 
    Deretter ber den bruker om et tall til, og printer ut resultatet av tommerTilCm med dette som parameter. 
    """
    tall1 = float(input("Skriv inn et tall: \n> "))
    tall2 = float(input("Skriv inn et tall: \n> "))
    print("Resultatet av addisjonen ble: " , addisjon(tall1, tall2))
    print("Resultatet av subtraksjonen ble: " , subtraksjon(tall1, tall2))
    print("Resultatet av divisjonen ble: " , divisjon(tall1, tall2))
    tommer = float(input("Skriv inn antall tommer: \n> "))
    print("{} tommer blir {} cm." .format(tommer, tommerTilCm(tommer)))


skrivBeregninger()




