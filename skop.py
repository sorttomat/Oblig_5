def minFunksjon():
    for x in range(2):
        c = 2
        print(c)
        c += 1
        b = 10
        b += a
        print(b)
    return(b)

def hovedprogram():
    a = 42
    b = 0
    print(b)
    b = a
    a = minFunksjon()
    print (b)
    print (a)

"""
minFunksjon defineres. Deretter defineres hovedprogram. Ingen av disse funksjonene
tar inn noen parametre. Forst blir hovedprogram() kalt paa:

Variablene a og b blir tilordnet verdiene 42 og 0. b, altsa 0, blir printet ut.
Naa blir b tilordnet den samme verdien som a, altsaa 42. De peker naa paa samme verdi.
a faar deretter en ny verdi, nemlig resultatet fra funksjonen minFunksjon() (eller det prover 
hvertfall programmet aa faa til).

Ettersom minFunksjon() har blitt kalt paa, gaar vi inn i den. Forst gaar vi inn i 
en forlokke, som tilsammen skal skjore 2 ganger:
1. variablen c blir tilordnet verdien 2. Denne printes ut. Deretter blir verdien til c
oekt med 1, og er naa 3. Variablen b faar verdien 10, og programmet prover deretter aa 
addere b med a. Dette gaar ikke, for variablen a finnes kun i hovedprogram(), og er ikke global.
Programmet stopper opp her. 
"""