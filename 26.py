

stipendi = []
while True:
	stipendio = float(input("inserisci uno stipendio, per stoppare scrivi -1"))
	if stipendio == -1:
		break
	else:
		stipendi.append(stipendio)
        
totdipendenti = len(stipendi)
somma = sum(stipendi)
media = somma / totdipendenti
print("La media degli stipendi è", media)			



