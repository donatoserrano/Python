"""
Scrivi un programma che chiede all'utente
il nome di un social network che utilizza abiutalmente
e la relativa password di accesso.
Il programma a questo punto apre un file
e scrive al suo interno una riga
contenente social e password
separati da un carattere a piacere.
Attenzione: ogni volta che il programma viene riavviato
e i nuovi social e password vengono inseriti,
la nuova riga che li conterrà venga AGGIUNTA al file.
"""

with open("social credentials.txt", "a", encoding="utf-8") as file:
    file.write(f"{input("Inserisci il nome del social: ").strip().capitalize()} = {input("Inserisci la password: ").strip()}\n")