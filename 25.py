candidato1= input("nome del primo candidato")
candidato2 = input("nome del secondo candidato")
punteggio1= int(input("punteggio del primo candidato"))
punteggio2 = int(input("punteggio del secondo candidato"))
nomi = [candidato1, candidato2]
nomi.sort()
punteggio = [punteggio1, punteggio2]
nomi.sort()
if punteggio1 > punteggio2:
   print (nomi,candidato1,candidato2)
if punteggio2 > punteggio1:
   print (nomi,candidato2,candidato1)