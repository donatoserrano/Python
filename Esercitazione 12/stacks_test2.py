"""
Inizializza una struttura dati adatta a gestire
una collezione di siti web visitati (stringhe)
Ora definisci un ciclo infinito in cui
viene richiesto all'utente quale sito vuole visitare.
Il sito immesso viene aggiunto alla collezione.
Se però l'utente immette il carattere <
significa che vuole tornare indietro al sito precedente,
allora rimuovi l'ultimo sito dalla collezione.
A fine iterazione di ciclo, 
stampa il sito in cui l'utente si trova attualmente.
"""
#errori non gestiti
from collections import deque

website_stack = deque()
user_choice = None

while user_choice != "Stop":
    user_choice = input("Digita il sito che vuoi visitare. Se vuoi tornare al sito precedente digita '<', se vuoi smettere di navigare digita 'Stop'\n").strip().capitalize()
    if user_choice != "<" and user_choice != "Stop":
        website_stack.append(user_choice)
    elif user_choice == '<':
        website_stack.pop()
    
print(f"Navigazione terminata: ti trovi su {website_stack[-1]}.")