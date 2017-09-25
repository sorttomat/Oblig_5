infile = open("temperatur.txt", "r")

temperaturer = []

for temp in infile:
    temp = temp.strip("\n")
    temperaturer.append(float(temp))

infile.close()

def gjennomsnitt(liste):
    sumListe = 0
    for elem in liste:
        assert type(elem) is float,  "TypeError"
        sumListe += elem
    return sumListe/len(liste)

print("Gjennomsnittstemperaturen er: ", gjennomsnitt(temperaturer))