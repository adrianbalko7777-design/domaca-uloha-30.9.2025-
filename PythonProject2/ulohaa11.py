# Naprogramuj funkciu, ktorá vypíše všetky čísla od 0-N, ktoré sú deliteľné siedmymi a štyrmi.

x = int(input('zadaj cislo N'))

for i in range(1,x):
    if i % 7 == 0:
        print(i)
    if i % 4 == 0:
        print(i)