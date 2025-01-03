"""
Programma per la gestione e modifica di una lista di album musicali.
"""
from album import Album
from music_library import MusicLibrary


while True:
    user_choice = input("Benvenuto, qui puoi gestire i tuoi album, scegli cosa vuoi fare.\n1. Aggiungere un album.\n2. Rimuovere un album\n3. Vedere la lista degli album\n4. Chiudere il programma.")
    if user_choice == 1:

