"""
Hai i seguenti numeri binari:
0b1011
0b0101
Utilizza fra loro un operatore bitwise,
affinchè il risultato sia un numero binario
con tutti i bit settati a 1 
eccetto l'ultimo bit (a destra)
"""

register_1 = 0b1011
register_2 = 0b0101
register_3 = (register_1 ^ register_2)
print(bin(register_3))