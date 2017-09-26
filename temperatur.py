"""
Dette programmet leser inn en fil med temperaturer, for saa aa bruke innholdet i filen til aa regne
ut gjennomsnittstemperaturen. 
"""

def gjennomsnitt(liste):
    """
    Funksjon som returnerer gjennomsnittet av tallene i en liste. 
    """
    sumListe = 0
    for elem in liste:
        assert type(elem) is float,  "TypeError"
        sumListe += elem
    return sumListe/len(liste)


infile = open("temperatur.txt", "r")
linjer = infile.readlines()
infile.close()

temperaturer = []
for linje in linjer:
    temp = linje.strip("\n")
    temperaturer.append(float(temp))



print("Gjennomsnittstemperaturen er: ", gjennomsnitt(temperaturer))