""" 
Scrivi un programma che richiede all'utente il suo anno di nascita.
Usa l'anno di nascita per calcolare l'età dell'utente.
Infine, stampa l'età dell'utente a schermo.
"""

year = int(input("Inserisci il tuo anno di nascita "))
age = 2024 - year
print("La tua età è di", age, "anni")

"""
All'esercizio precedente aggiungi una variabile booleana
che rappresenta se l'utente è maggiorenne.
Per assegnare un valore alla variabile
controlla se l'utente ha età maggiore o uguale a 18.
Infine, stampala sul terminale
"""

is_adult = age >= 18
print("Sei maggiorenne?", is_adult)

""" 
All'esercizio precedente aggiungi una variabile booleana, 
che rappresenta se l'utente è maggiorenne
e se possiede la patente,
salva tale informazione su una nuova variabile 
e poi stampala a schermo
"""

hasLicense = False and is_adult
print("Hai la patente?", hasLicense)