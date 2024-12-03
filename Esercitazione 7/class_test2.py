"""
Alla classe dell'esercizio precedente
aggiungi un nuovo metodo,
che servirà ad applicare uno sconto al libro.
Il metodo perciò, prevede un parametro
che rappresenta la percentuale da scontare
e, in base ad essa riduce il prezzo originario
(rappresentato dall'attributo di istanza).
Una volta chiamato il metodo su un oggetto,
controlla se il prezzo è stato aggiornato correttamente.
Per controprova, controlla anche che il prezzo,
sull'altro oggetto sia rimasto invariato.
P.S.
Per calcolare il prezzo scontato, si può usare la formula:
Prezzo Scontato = Prezzo Originale x (100 - Percentuale) / 100
Ad esempio se il Prezzo Originale è 15.9
e passo come Percentuale di sconto 30
il prezzo finale dev'essere pari a 11.13.
"""

class Libro:
    def __init__(self, title, author, publication_year, price):
        self.title = title
        self.author = author
        self.publication_year = publication_year
        self.price = price
    
    def print_book(self):
        print(f"{self.title}, scritto da {self.author}, pubblicato nel {self.publication_year} al prezzo di {self.price} euro.")

    def discount_book(self, discount_percentage):
        discounted_price = self.price*(100-discount_percentage)/100
        return discounted_price
    

book1 = Libro("Divina Commedia", "Dante Alighieri", "1600", 20)
book2 = Libro("Harry Potter", "J. K. Rowling", 1980, 32)
book1.print_book()
book2.print_book()
discounted_percentage = int(input("Inserisci la percentuale di sconto. "))
book1.price = book1.discount_book(discounted_percentage)
print(f"Prezzo scontato del libro '{book1.title}': {book1.price}")