# Naprogramuj funkciu, ktorá v intervale od  <začiatok,  koniec>  zistí počet čísel, ktoré sú deliteľné ôsmimi

x = int(input('Zadaj zaciatocne cislo'))
y = int(input('Zadaj konecne cislo'))

for i in range(x,y):
    if i % 8 == 0:
        print(i)

