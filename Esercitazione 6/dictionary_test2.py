"""
Definisci due dizionari che rappresentano una persona,
avente il campo nome, ed altri dati a piacere.
Entrambi i dizionari possiedono il campo età
ma non è valorizzato.

Definisci una funzione che prende in input dall'utente
l'anno di nascita,
calcola l'età e la restituisce.
Nel messaggio di input va stampato il nome della persona,
bisogna perciò passarlo alla funzione come argomento.
Per calcolare l'età servirà l'anno attuale,
che deve esser passato anch'esso alla funzione.

Infine, chiama due volte la funzione,
per valorizzare il campo età sui due dizionari.
"""
#funzione per calcolare l'età in base all'anno corrente
def calculate_age(person, year):
    print(f"Inserisci l'anno di nascita di {person["name"]}")
    person["age"] = int(input())
    return year-person["age"]

person_1 = {
    "name": "Fabio",
    "surname": "Spigoli",
    "age": None
}
person_2 = {
    "name": "Fabio",
    "surname": "Spigoli",
    "age": None
}

print(f"{person_1["name"]} ha {calculate_age(person_1, 2024)} anni")
print(f"{person_2["name"]} ha {calculate_age(person_1, 2024)} anni")