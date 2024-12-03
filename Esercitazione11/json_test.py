"""
Converti in un file json
il file di testo generato
negli esercizi precedenti (senza alterare l'originale)
Inizialmente crea un dizionario vuoto, quindi
apri il file di testo in lettura
accedi ciclicamente a ogni riga e dividila
(metodo split "=")
per ottenere chiave (social) e valore (password).
Aggiungi al dizionario ciascuna coppia chiave-valore.
Infine apri un nuovo file di scrittura
e scrivi il dizionario su di esso
serializzandolo col metodo json.dump.
"""

import json
social_passwords = {}

with open("social credentials.txt", "r", encoding="utf-8") as file:
    for line in file:
        split_string = line.strip().split(" = ")
        social_passwords[split_string[0]] = split_string[1]

with open("social credentials.json", "w", encoding="utf-8") as file:
    json.dump(social_passwords, file, ensure_ascii=False, indent= 4)