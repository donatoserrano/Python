"""
Classe per la gestione della libreria musicale
"""
import json
from album import Album 

class MusicLibrary:

    def __init__(self, file_name="music.library.json"):
        self.file_name = file_name
        self.albums = self.load_from_file()

    def add_album(self):
        #

    def remove_album(self):
        #
    
    def load_to_file(self):
        with open(self.file_name, "w") as file:
            json.dump(self.albums, self.file_name, ensure_ascii=False, indent=4)



    #aggiungere controllo errori
    def load_from_file(self):
        with open(self.file_name, "r") as file:
            albums_data = json.load(file)
            return [Album(album["title"], album["author"], album["genre"], album["release_date"]) for album in albums_data]