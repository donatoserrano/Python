"""
Crea una classe che rappresenta una persona,
e possiede gli attributi di istanza nome e età.
Ora crea una classe che rappresenta un regista,
che eredita dalla classe persona,
e possiede un attributo di istanza in più
che indica un film famoso che ha girato.

Istanzia un oggetto della superclasse,
poi un oggetto della sottoclasse,
e verifica quali attributi
sono accessibili su di essi.
"""

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        print(f"Nome: {self.name}, Età: {self.age}.")

class Director(Person):
    def __init__(self, name, age, famous_movie):
        super().__init__(name, age)
        self.famous_movie = famous_movie

    def __str__(self):
        print(f"Nome regista: {self.name}, Età: {self.age}, Film più famoso: {self.famous_movie}")

giacomo = Person("Giacomo", 39)
pierino = Director("Pierino", 33, "Harry Potter")
giacomo.__str__()
pierino.__str__()
