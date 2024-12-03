"""
Definisci una lista che contenga 3 mete turistiche.
Stampale tutte a schermo e chiedi all'utente
dove desidera andare.
Per scegliere dovrà immettere 
l'indice dell'elemento della lista,
in questo caso un numero da 0 a 2.
Stampa a schermo un augurio di buon viaggio,
contenente la destinazione scelta.

Lancia il programma e tenta di farlo andare in errore,
così da trovare le eccezioni che
potrebbero verificarsi nel processo.
"""

destinations = ["Avana", "Tokyo", "Rio de Janeiro"]
for index, destination in enumerate(destinations):
    print(f"Destinazione {index+1}: {destination}")

try:
    user_choice = int(input("Digita il numero della destinazione desiderata ").strip()) - 1
    if user_choice < 0 or user_choice > 2:
        raise IndexError()
except ValueError:
    print("Errore: Non hai inserito un numero intero.")
except IndexError:
    print("Errore: Hai inserito un numero fuori range")
except Exception as e:
    print(f"Errore: {e} {type(e)}")
else:
    print(f"Destinazione scelta: {destinations[user_choice]}, ti auguriamo buon viaggio!")