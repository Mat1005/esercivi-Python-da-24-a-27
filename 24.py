candidato1 = input("Come si chiama il primo candidato?")
candidato2 = input("Come si chiama il secondo candidato?")
voti1 = int(input("Quanti voti ha preso il primo candidato?")) 
voti2 = int(input("Quanti voti ha preso il secondo candidato?"))
Votitot = voti1 + voti2
pervoti1 = voti1*100/Votitot 
pervoti2 = voti2*100/Votitot 
if pervoti1 > pervoti2:
    print("Vince",candidato1,"con il",pervoti1,"dei voti")
if pervoti2 > pervoti1:
    print("Vince",candidato2,"con il",pervoti2,"dei voti")