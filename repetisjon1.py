mineOrd = []

def slaaSammen(streng1, streng2):
    assert type(streng1) is str, "TypeError"
    assert type(streng2) is str, "TypeError"

    return streng1 + streng2

def skrivUt(liste):
    assert type(liste) is list, "TypeError"
    for elem in liste:
        print(elem)


def skrivUtAlternativer():
    print("Hva onsker du aa gjore?\nFor aa slaa sammen to ord: Press i\nFor aa skrive ut listen: Press u\nFor aa avslutte: Press s\n> ")

def taImotInput():
    skrivUtAlternativer()
    svar = input()
    while svar != "i" and svar != "u" and svar != "s":
        print("Det forsto jeg ikke.")
        skrivUtAlternativer()
        svar = input()
    return svar

svar = taImotInput()
while svar != "s":
    if svar == "i":
        print("Hvilke to strenger vil du slaa sammen?")
        streng1 = input("Forste streng: ")
        streng2 = input("Andre streng: ")
        mineOrd.append(slaaSammen(streng1, streng2))
        print("Strengene er slaatt sammen, og ligger naa i listen.")
    
    elif svar == "u":
        skrivUt(mineOrd)
    
    svar = taImotInput()



        
        

