"""
Dette programmet spor brukeren om hva hen vil gjore, og utifra svaret utforer programmet
handlinger.
"""

def slaaSammen(streng1, streng2):
    """
    Funksjon som slaar sammen to strenger, etter aa ha sjekket om begge parametrene
    er strenger.
    """
    assert type(streng1) is str, "TypeError"
    assert type(streng2) is str, "TypeError"
    return streng1 + streng2

def skrivUt(liste):
    """
    Funksjon som forst sjekker om parameteret er en liste, for saa a skrive ut 
    innholdet i listen element for element. 
    """
    assert type(liste) is list, "TypeError"
    for elem in liste:
        print(elem)


def skrivUtAlternativer():
    """
    Prosedyre som printer ut menyen. 
    """
    print("Hva onsker du aa gjore?\nFor aa slaa sammen to ord: Press i\nFor aa skrive ut listen: Press u\nFor aa avslutte: Press s\n> ")

def taImotInput():
    """
    Funksjon som forst kaller paa skrivUtAlternativer(), for saa aa ta imot svaret fra brukeren. 
    Dersom svaret ikke er et av alternativene, vil den sporre om svar igjen helt til svaret 
    er et av de riktige. 
    """
    skrivUtAlternativer()
    svar = input()
    while svar != "i" and svar != "u" and svar != "s":
        print("Det forsto jeg ikke.")
        skrivUtAlternativer()
        svar = input()
    return svar


mineOrd = []
svar = taImotInput()
while svar != "s": #Mens svaret ikke er "s", kjores koden under:
    if svar == "i":
        print("Hvilke to strenger vil du slaa sammen?")
        streng1 = input("Forste streng: ")
        streng2 = input("Andre streng: ")
        mineOrd.append(slaaSammen(streng1, streng2))
        print("Strengene er slaatt sammen, og ligger naa i listen.")
    
    elif svar == "u":
        skrivUt(mineOrd)
    
    svar = taImotInput() #Etter hver "runde", kjores taImotInput(). Helt til brukeren taster inn "s".



        
        

