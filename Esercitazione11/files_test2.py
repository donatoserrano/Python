"""
Modifica il programma precedente,
aggiungendo la funzionalità di lettura.
All'avvio il programma chiede all'utente
se desidera aggiungere un nuovo social e password,
o se desidera leggere quelli già presenti.
Se desidera aggiungere, procedi come in precedenza.
Se desidera leggere, apri il file in lettura,
e stampa a schermo ognuna delle righe
contenenti social e password,
precedute da un trattino o un altro carattere a piacere.
"""

def socialAdd():
    with open("social credentials.txt", "a", encoding="utf-8") as file:
        file.write(f"{input("Inserisci il nome del social: ").strip().capitalize()} = {input("Inserisci la password: ").strip()}\n")

def socialRead():
    with open("social credentials.txt", "r", encoding="utf-8") as file:
        for line in file:
            print(f"- {line.strip()}")

user_choice = int(input("Digita 1 se vuoi aggiungere un altro social, 2 se vuoi leggere i social scritti fin'ora "))
if user_choice == 1:
    socialAdd()
elif user_choice == 2:
    socialRead()
else:
    print("Scelta non valida...")