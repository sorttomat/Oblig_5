def addisjon(adder1, adder2):
    return adder1 + adder2

print(addisjon(1, 4))

def subtraksjon(minuend, subtrahend):
    return minuend - subtrahend

assert subtraksjon(10, 5) == 5, "Naa ble det feil"
assert subtraksjon(5, -10) == 15, "Naa ble det feil"
assert subtraksjon(-2, -8) == 6, "Naa ble det feil"

def divisjon(dividend, divisor):
    return dividend/divisor

assert divisjon(10, 5) == 2, "Naa ble det feil"
assert divisjon(-15, 5) == -3,  "Naa ble det feil"
assert divisjon(-8, -2) == 4, "Naa ble det feil"

def tommerTilCm(antallTommer):
    assert antallTommer > 0, "Antall tommer er mindre eller lik 0."
    return antallTommer * 2.54

print(tommerTilCm(54))

def skrivBeregninger():
    tall1 = float(input("Skriv inn et tall: \n> "))
    tall2 = float(input("Skriv inn et tall: \n> "))
    print("Resultatet av addisjonen ble: " , addisjon(tall1, tall2))
    print("Resultatet av subtraksjonen ble: " , subtraksjon(tall1, tall2))
    print("Resultatet av divisjonen ble: " , divisjon(tall1, tall2))
    tommer = float(input("Skriv inn antall tommer: \n> "))
    print("{} tommer blir {} cm." .format(tommer, tommerTilCm(tommer)))

skrivBeregninger()




