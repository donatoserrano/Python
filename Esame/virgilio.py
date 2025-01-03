"""
 La classe, dovrà chiamarsi Virgilio
 e dovrà essere definita all’interno del file virgilio.py.
 La classe dovrà avere un attributo di istanza chiamato directory,
 inizializzato nel metodo costruttore.
"""
import os
import json


class Virgilio:

    def __init__(self):
        self.directory = "c:/Users/Utente/Desktop/Python/Esame/canti"

    # 16.  Modifica il metodo read_canto_lines affinché, verifichi se canto_number
    # ha un valore incompatibile col numero dei Canti (che va da 1 a 34)
    # In tal caso solleva un'eccezione personalizzata chiamata CantoNotFoundError,
    # che ha come messaggio: canto_number must be between 1 and 34.
    # Tale eccezione va definita all’interno della classe Virgilio.
    class CantoNotFoundError(Exception):
        def __init__(self, message):
            self.message = message
            super().__init__(self.message)

    # 1. Crea un metodo chiamato read_canto_lines che ha il parametro canto_number.
    # Il metodo legge uno dei 34 file di testo rappresentanti i Canti.
    # Il numero del canto da leggere è rappresentato da canto_number.
    def read_canto_lines(self, canto_number, strip_lines=False, num_lines=None):

        if type(canto_number) is not int:
            raise TypeError("canto_number must be an integer")

        if canto_number < 1 or canto_number > 34:
            raise Virgilio.CantoNotFoundError(
                "canto_number must be between 1 and 34.")

        try:
            file_path = os.path.join(
                self.directory, f"Canto_{canto_number}.txt")
            with open(file_path, "r", encoding="utf-8") as file:
                lines = file.readlines()
        except Exception as e:
            print(f"error while opening {file_path}")

        # Aggiunta parametro opzionale strip_lines
        if strip_lines:
            for line in lines:
                line = line.strip()

        # Aggiunta parametro opzionale num_lines
        if num_lines:
            for i in range(num_lines):
                new_lines = line[i]
            return new_lines

        return lines

    # 2. Crea un metodo chiamato count_verses che ha il parametro canto_number.
    # Il metodo restituisce il numero di versi (righe) del Canto specificato da canto_number.
    def count_verses(self, canto_number):
        return len(self.read_canto_lines(canto_number))

    # 3. Crea un metodo chiamato count_tercets che ha il parametro canto_number.
    # Il metodo restituisce il numero (int) di terzine del Canto scelto.
    def count_tercets(self, canto_number):
        return int(self.count_verses(canto_number)/3)

    # 4. Crea un metodo chiamato count_word
    # che ha il parametro canto_number ed il parametro word.
    # Il metodo restituisce il numero di volte che la parola word si presenta nel Canto scelto
    def count_word(self, canto_number, word):
        lines = self.read_canto_lines(canto_number)
        found = 0
        for line in lines:
            # Utilizzo words per dividere ogni parola per evitare di contare parole composte
            words = line.split()
            found += words.count(word)
        return found

    # (+)Creo list con tutti i versi
    def get_verses(self, canto_number):
        lines = self.read_canto_lines(canto_number)
        verses_list = []
        for line in lines:
            verses_list.append(line.strip())
        return verses_list

    # 5. Crea un metodo chiamato get_verse_with_word
    # che ha il parametro canto_number ed il parametro word.
    # Il metodo restituisce il primo verso (partendo dall’inizio) del Canto scelto,
    # in cui è presente la parola word.
    def get_verse_with_word(self, canto_number, word):
        verses_list = self.get_verses(canto_number)
        for verse in verses_list:
            words = verse.split()
            if word in words:
                found_verse = verse
                break

        if found_verse:
            return verse
        else:
            return None

    # 6. Crea un metodo chiamato get_verses_with_word
    # che ha il parametro canto_number ed il parametro word.
    # Il metodo restituisce una lista di tutti i versi del Canto scelto
    # in cui è presente la parola word.
    def get_verses_with_word(self, canto_number, word):
        verses_list = self.get_verses(canto_number)
        found_verses_list = []
        for verse in verses_list:
            words = verse.split()
            if word in words:
                found_verses_list.append(verse)
        return found_verses_list

    # 7. Crea un metodo chiamato get_longest_verse che ha il parametro canto_number.
    # Il metodo restituisce il verso più lungo del Canto scelto.
    # Se ci sono più versi con la stessa lunghezza,
    # restituisce il primo che trova partendo dall’inizio del Canto
    def longest_verse(self, canto_number):
        verses_list = self.get_verses(canto_number)
        longest_verse = ""
        # Controllo i versi partendo dall'ultimo
        for i in range(len(verses_list)-1, -1, -1):
            if len(longest_verse) < len(verses_list[i]):
                longest_verse = verses_list[i]
        return longest_verse

    # 8. Crea un metodo chiamato get_longest_canto.
    # Il metodo restituisce un dizionario con due coppie chiave-valore.
    # La chiave canto_number ha come valore un numero intero,
    # che rappresenta il Canto con più versi dell’intero Inferno.
    # La chiave canto_len ha come valore un numero intero,
    # che rappresenta quanti versi possiede tale Canto
    def get_longest_canto(self):
        longest_canto = {
            "canto_number": 0,
            "canto_len": 0
        }
        for i in range(1, 35):
            if self.count_verses(i) > longest_canto["canto_len"]:
                longest_canto["canto_len"] = self.count_verses(i)
                longest_canto["canto_number"] = i
        return longest_canto

    # 9. Crea un metodo chiamato count_words che ha il parametro canto_number ed il parametro words.
    # Tale parametro è una lista di parole da conteggiare all’interno del Canto scelto.
    # Il metodo deve infatti restituire un dizionario dove ogni coppia chiave-valore
    # ha come chiave la parola e come valore il numero di volte che essa si presenta nel Canto.
    def count_words(self, canto_number, words):
        word_counts = {}
        for word in words:
            word_counts[word] = self.count_word(canto_number, word)

        file_path = os.path.join(
            "c:/Users/Utente/Desktop/Python/Esame", "word_counts.json")
        with open(file_path, "w", encoding="utf-8") as json_file:
            json.dump(word_counts, json_file, ensure_ascii=False, indent=4)

        return word_counts

    # 10. Crea un metodo chiamato get_hell_verses che restituisce una lista
    # contenente tutti i versi di tutti e 34 Canti i dell’Inferno,
    # in ordine dal primo all’ultimo

    def get_hell_verses(self):
        all_verses_list = []
        for i in range(1, 35):
            all_verses_list.append(self.get_verses(i))
        return all_verses_list

    # 11. Crea un metodo chiamato count_hell_verses che restituisce
    # un int rappresentante il numero totale di versi contenuti nell’Inferno.
    def count_hell_verses(self):
        total_verses = 0
        for i in range(1, 35):
            total_verses += self.count_verses(i)
        return total_verses

    # 12. Crea un metodo chiamato get_hell_verse_mean_len che restituisce
    # un float rappresentante la lunghezza media dei versi dell’inferno.
    # Il verso deve essere privato di spazi o caratteri affini presenti all’inizio e alla fine.
    # Gli spazi fra le parole invece, non devono essere eliminati, ma conteggiati anch’essi.
    def get_hell_verse_mean_len(self):
        total_length = 0
        for i in range(1, 35):
            verses_list = self.get_verses(i)
            for verse in verses_list:
                total_length += len(verse.strip())
        return total_length/self.count_hell_verses()