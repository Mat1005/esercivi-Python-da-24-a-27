veicoli = []
while True:
	veicolo = int(input("inserisci numero veicoli transitati in un giorno , per stoppare scrivi 0"))
	if veicolo == 0:
		break
	else:
		veicoli.append(veicolo)
        
Periodo = len(veicoli)
somma = sum(veicoli)

print("Il totale dei veicoli transitati in",Periodo,"giorni è",somma)			

