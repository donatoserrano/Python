"""
Implementa il trova e sostituisci.
Richiedi all'utente quale parola vuole trovare
e con quale vuole sostituirla.
Applica tali sostituzioni ad un testo
Infine stampa il testo modificato sul terminale
senza modificare il testo iniziale
"""

text = '''Harry si sentì leggero mentre saliva sulla scopa volante.
Per la prima volta, Harry provò il brivido del decollo.
Quella del volo, diventò immediatamente la più grande passione di Harry.'''
print("Testo originale: ")
print(text)
print()

world_to_replace = input("Quale parola desideri modificare? ")
new_word = input("Con quale parola vuoi sostituirla? ")
print()

modified_text = text.replace(world_to_replace, new_word)
print("Testo modificato:")
print(modified_text)