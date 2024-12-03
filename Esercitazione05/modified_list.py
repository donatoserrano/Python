"""
Crea una lista della spesa che contenga
alcuni articoli a piacere.
Ordina gli articoli "alfabeticamente"
e stampali tutti a schermo,
ognuno di essi preceduto da un trattino.
Ora chiedi all'utente un nuovo articolo
da aggiungere.
Se l'utente non inserisce nulla,
stampa un messaggio di errore.
Se l'utente inserisce un articolo già presente,
stampa un messaggio di errore.
Se inserisce un articolo corretto,
aggiungilo alla lista.
Al termine del programma stampa tutti gli articoli
(ordinati alfabeticamente)

Modifica il programma: 
se l'utente inserisce un articolo già presente,
chiedi all'utente se vuole rimuoverlo.
In caso affermativo, procedi alla rimozione.

Modifica il programma:
L'utente deve poter inserire più articoli alla volta,
separandoli col carattere |
In tal caso, il programma converte tale stringa
in una lista di articoli, i quali vengono
aggiunti alla lista iniziale.
"""
articles = ["Pane", "Pasta", "Carote", "Cipolle", "Vino"]
articles.sort()
print("Lista della spesa iniziale:")
print(*articles, sep=" - ")

#Gestione e separazione stringa utente
user_list = input("Inserisci degli articoli separati da '|'. ")
user_articles = user_list.split("|").copy()
for article in user_articles:
    article = article
#Controlli
if not user_list:
    print("Non hai inserito nessun articolo.")
else:
    print("Articolo aggiunto!")
    articles.extend(user_articles)
    
articles.sort()
print("Lista finale:")
print(*articles, sep=" - ")
