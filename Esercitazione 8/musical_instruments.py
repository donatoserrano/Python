"""
Definisci una classe che rappresenti
uno strumento musicale,
ad esempio una chitarra, un piano, etc...
Assegna alla classe almeno due attributi d'istanza
e almeno due attributi di classe, a piacere.

Istanzia un oggetto della classe e applica
il principio della Instrospection:
con le funzioni hasattr e dir,
verifica quali attributi sono accessibili
sull'oggetto e quali sulla classe.
"""

class Instrument:
    total_instruments = 0

    def __init__(self, name, price):
        self.name = name
        self.price = price
        Instrument.total_instruments += 1

chitarra = Instrument("Chitarra", 100)
tamburo = Instrument("Tamburo", 45)
print(hasattr(Instrument, "total_instruments"))
print(hasattr(chitarra, "name"))
print(hasattr(tamburo, "price"))
print(dir(chitarra))
print(dir(tamburo))
