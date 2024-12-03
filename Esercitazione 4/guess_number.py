"""
Salva un numero a piacere su una variabile,
poi chiedi all'utente di indovinarlo.
Il numero deve essere da 0 a 9.
Controlla se l'utente lo indovina,
lo sbaglia,
o se inserisce un numero fuori range,
e stampa a schermo un messaggio opportuno.
Poi aggungi la possibilità di fare al massimo
5 tentativi.
"""

number_to_guess = 7
user_number = None
print("Prova a indovinare il numero da 0 a 9.")

for tries in range(1, 6):
    user_number = int(input(f"Tentativo numero: {tries}. Inserisci un numero. "))
    if user_number < 0 or user_number > 9:
        print("Hai inserito un numero fuori range, riprova.")
    elif user_number != number_to_guess:
        print("Numero sbagliato, riprova.")
    elif user_number == number_to_guess:
        print("Numero indovinato!!")
        break
else:
    print("Tentativi terminati... hai perso!")