from virgilio import Virgilio

x = 1

virgy = Virgilio()
# Test 1. V
"""print("Test 1")
lines = virgy.read_canto_lines(x)
for line in lines:
    print(line)"""
# Test 2. V
print("Test 2")
print(virgy.count_verses(x))
# Test 3. V
print("Test 3")
print(virgy.count_tercets(x))
# Test 4. V
print("Test 4")
word = "per"
print(f"La parola {word} compare {virgy.count_word(x, word)} volte.")
#Test 5. V
print("Test 5")
print(virgy.get_verse_with_word(1, word))
#Test 6. V
verses = virgy.get_verses_with_word(1, word)
"""print("Test 6")
for verse in verses:
    print(f"{verse}\n")"""
#Test 7. V
print("Test 7")
print(f"Il verso più lungo è questo:\n {virgy.longest_verse(1)}")
#Test 8. V
print("Test 8")
print(f"Il canto con più versi è il {virgy.get_longest_canto()["canto_number"]}, lungo {virgy.get_longest_canto()["canto_len"]} versi")
#Test 9. V
print("Test 9")
for key, value in virgy.count_words(1, ["per", "dai", "selva"]).items():
    print(f"{key} : {value}")
#Test 10. V
"""print("Test 10")
lines = virgy.get_hell_verses()
for line in lines:
    print(f"{line}")"""
#Test 11. V
print("Test 11")
print(f"Nell'inferno ci sono {virgy.count_hell_verses()} versi")
#Test 12. V
print("Test 12")
print(f"Lunghezza media versi inferno: {virgy.get_hell_verse_mean_len()}")