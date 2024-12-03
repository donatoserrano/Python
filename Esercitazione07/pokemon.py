"""
Crea una classe Pokemon coi seguenti attributi:
Nome, Salute e Forza.
Implementa un metodo di attacco che permetta
a un Pokemon di attaccarne un altro,
riducendo la Salute dell'avversario.
(al metodo passeremo come argomento un oggetto Pokemon)
La Salute dell'avversario viene ridotta
di un valore pari alla Forza dell'attaccante.
Il metodo infine stampa un messaggio,
con alcuni dettagli sull'attacco, ad esempio:
Pikachu attacca Charizard causando 15 danni!

Completata la classe, istanzia due Pokemon
e falli attaccare l'un l'altro, quante volte desideri.
Dopo il combattimento, stampa la Salute
di entrambi, per vedere se è coerente con gli attacchi.
"""

class Pokemon:
    def __init__(self, name, health, strenght):
        self.name = name
        self.health = health
        self.strenght = strenght

    def attack(self, Enemy):
        Enemy.health = Enemy.health - self.strenght
        print(f"{self.name} attacca {Enemy.name} infliggendo {self.strenght} danni!")

    def winning_message(self, Enemy):
        print(f"{self.name} sconfigge {Enemy.name} con {self.health}PS rimanenti!")



pikachu = Pokemon("Pikachu", 80, 30)
charizard = Pokemon("Charizard", 110, 25)

while pikachu.health > 0 and charizard.health > 0:
    pikachu.attack(charizard)
    input()
    if charizard.health > 0:
        charizard.attack(pikachu)
        input()

if charizard.health <= 0:
    pikachu.winning_message(charizard)
else:
    charizard.winning_message(pikachu)