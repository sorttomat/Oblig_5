"""
Dette programmet tar nå inn en tekstfil som heter "a_study_in_scarlet.txt", lager ord-objekter
av hvert ord (det samme ordet blir ikke laget til et objekt flere ganger), som ligger lagret i ordliste-klassen.
"""

class Ord:
    """
    Denne klassen inneholder de lokale variablene "ord" og "antall". 
    """
    def __init__(self, ord): 
        self.ord = ord
        self.antall = 1

    def oekAntall(self):
        """
        Metode som oeker ordets antall med 1. 
        """
        self.antall += 1
    
    def getOrd(self):
        """
        Metode som returnerer ordet. Dette er nodvendig for aa kunne
        faa selve ordet ut, ettersom variablen "ord" er lokal og ikke kan 
        kalles paa utenifra. 
        """
        return self.ord

    def getAntall(self):
        """
        Metode som returnerer antallet instanser av ordet. 
        """
        return self.antall


class Ordliste():
    """
    Denne klassen inneholder den lokale variablen "liste", som inneholder alle 
    ord-objektene. 
    """
    def __init__(self):
        self.liste = []
    
    def lesInnBok(self, boktittel):
        """
        Metode som leser inn en fil, gjor hver linje om til kun ett ord (tar vekk unodvendige
        tegn o.l), og kaller paa metoden leggTilOrd() for hvert ord. 
        """
        bok = open(boktittel, "r")
        linjer = bok.readlines() #Leser alle linjene, og legger dem i "linjer"
        for linje in linjer: 
            linje = linje.strip("\n")
            linje = linje.lower()
            self.leggTilOrd(linje)
    
    def leggTilOrd(self, ord):
        """
        Metode som, hvis ordet allerede finnes i ordlisten, kaller paa metoden 
        oekAntall(). Hvis ordet ikke finnes i ordlisten, lager den et ordobjekt av ordet
        og legger dette inn i ordlisten (liste).
        """
        for ordObjekt in self.liste:
            if ordObjekt.getOrd() == ord:
                ordObjekt.oekAntall()
                break 
        else:
            self.liste.append(Ord(ord))
    
    def printOrdliste(self):
        """
        Metode som printer ut alle objektene i ordlisten, sortert etter antall forekomster.
        Den kaller paa getOrd() og getAntall(), og printer ut resultatet av disse kallene. 
        """
        for ordObjekt in sorted(self.liste, key = self.getAntallKey):
            print(ordObjekt.getOrd(), ordObjekt.getAntall())

    def printSortertOrdliste(self):
        """
        Metode som printer ut alle objektene i ordlisten, sortert etter alfabetisk rekkefolge. 
        """
        for ordObjekt in sorted(self.liste, key = self.getForsteBokstavKey):
            print(ordObjekt.getOrd(), ordObjekt.getAntall())

    def printOrd(self, ord):
        """
        Metode som printer ut informasjon om ett bestemt ord.
        """
        for ordObjekt in self.liste:
            if ordObjekt.getOrd() == ord:
                print("Det er {} instanser av ordet '{}'.".format(ordObjekt.getAntall(), ordObjekt.getOrd())) 

    def getAntallKey(self, ordObjekt):
        """
        Metode som brukes for aa kunne sortere ordlisten etter antall forekomster. 
        """
        return ordObjekt.getAntall()

    def getForsteBokstavKey(self, ordObjekt):
        """
        Metode som brukes for aa kunne sortere ordlisten etter forbokstav. 
        """
        return ordObjekt.getOrd()[0]


#Lager en instans av klassen Ordliste, og tester programmet:
ordliste = Ordliste()
ordliste.lesInnBok("a_study_in_scarlet.txt")
ordliste.printOrdliste()
ordliste.printSortertOrdliste()
ordliste.printOrd("a")
