"""
Alla classe dell'esercizio precedente,
aggiungi il metodo speciale str affinché,
quando l'oggetto viene stampato,
appaia un messaggio descrittivo a piacere.
"""

class Instrument:
    total_instruments = 0

    def __init__(self, name, price):
        self.name = name
        self.price = price
        Instrument.total_instruments += 1

    def __str__(self):
        return f"Strumento: {self.name}, prezzo: {self.price}."

chitarra = Instrument("Chitarra", 100)
tamburo = Instrument("Tamburo", 45)
print(hasattr(Instrument, "total_instruments"))
print(hasattr(chitarra, "name"))
print(hasattr(tamburo, "price"))
print(dir(chitarra))
print(dir(tamburo))
print(chitarra)
print(tamburo)