"""
Modifica l'esercizio della lezione precedente,
ma basandolo su un dizionario, invece che su una lista.
Il dizionario iniziale deve contenere
come chiave il prodotto da acquistare
e come valore la sua quantità.
All'utente sarà richiesto di inserire
sia il prodotto che la quantità.
Non è necessario ordinare il dizionario.
BONUS:
Se l'articolo è già presente,
chiedi di inserire la quantità
e aggiornala sul dizionario.
"""
#dizionario
items = {
    "fagioli": 3,
    "noci": 2,
    "mele": 10
}
#print iniziale
for item, quantity in items.items():
    print(f"{item} : {quantity} pezzi")
#richiesta utente
user_item = input("Aggiungi un articolo: ").lower().strip()
user_amount = int(input("Specifica la quantità: ").strip())
#controlli e variazioni
if not user_item or not user_amount:
    print("Errore: Non hai inserito alcun articolo")
elif user_item in items:
    print("Errore: Articolo già presente")
    print("Vuoi variarne la quantità? In caso positivo digita 'si'")
    if input() == "si":
        print("Inserisci la quantità:")
        items[user_item] = input()
else:
    print("Articolo aggiunto ✅")
    items[user_item] = user_amount
#stampa finale
for item, quantity in items.items():
    print(f"{item} : {quantity} pezzi")