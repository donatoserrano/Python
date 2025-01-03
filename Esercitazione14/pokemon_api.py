"""
Scrivi un programma che chiede all'utente
il nome di un Pokemon.
Invia una richiesta GET all'api pokeapi.co,
verifica se ha successo,
in caso affermativo, stampa a schermo
l'altezza, il peso e il tipo del Pokemon.
"""

import requests

user_pokemon_choice = input("Di quale Pokemon vuoi ottenere informazioni? ")
response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{user_pokemon_choice}")
pokemon_stats = response.json()

print(f"L'altezza del tuo pokemon è: {pokemon_stats["height"] / 10} metri")
print(f"Il peso è: {pokemon_stats["weight"] / 10} kg")

try:
    print(f"I tipi del tuo pokemon sono: {pokemon_stats["types"][0]["type"]["name"]}, {pokemon_stats["types"][1]["type"]["name"]}")
except IndexError:
    print(f"Il tipo del tuo pokemon è: {pokemon_stats["types"][0]["type"]["name"]}")
