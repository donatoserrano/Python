"""
Definisci una classe che rappresenta un libro.
La classe ha gli attributi di istanza
titolo, autore, anno pubblicazione e prezzo.
La classe ha anche un metodo che stampa,
con un messaggio a piacere, tutti i propri attributi.
Una volta completata la classe,
instanziane due oggetti, passando un argomento
per ciascun attributo di istanza.
Chiama su ciascuno dei due oggetti il metodo,
e verifica che il messaggio stampato sia corretto.
"""

class Libro:
    def __init__(self, title, author, publication_year, price):
        self.title = title
        self.author = author
        self.publication_year = publication_year
        self.price = price
    
    def print_book(self):
        print(f"{self.title}, scritto da {self.author}, pubblicato nel {self.publication_year} al prezzo di {self.price} euro.")
    

book1 = Libro("Divina Commedia", "Dante Alighieri", "1600", 20)
book2 = Libro("Harry Potter", "J. K. Rowling", 1980, 32)
book1.print_book()
book2.print_book()