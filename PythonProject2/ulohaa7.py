# Naprogramuj funkciu, ktorá vypíše všetky čísla od 1-N, ktoré sú deliteľné troma.

x = int(input('Zadaj cislo N'))

for i in range(1,x):
    if i % 3 == 0:
        print(i)