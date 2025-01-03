"""
Classe per la gestione dell'album
"""

class Album:
    
    def __init__(self, author, title, genre, release_date):
        self.author = author
        self.title = title
        self.genre = genre
        self.release_date = release_date

    def __str__(self):
        print(f"Album: {self.title} di {self.author}, rilasciato nel {self.release_date}, genere: {self.genre}")

    """def add_album(self):
        print("Inserisci i dati dell'album:")
        try:
            self.author = input("Chi è l'autore? ").strip().capitalize()
            self.title = input("Titolo dell'album? ").strip().capitalize()
            self.genre = input("Genere dell'album? ").strip().capitalize()
            self.release_date = input("Data di rilascio? ").strip().capitalize()
            if not self.author or not self.title or not self.genre or not self.release_date:
                raise ValueError()
        except ValueError:
            print("Errore, non hai inserito un dato.")"""