# Naprogramuj funkciu, ktorá vypíše pre čísla od <odkiaľ> <pokial> aj ich druhé odmocniny (zaokrúhlené na 2 des.miesta). Pričom hodnoty <odkiaľ> <pokial> sú parametre funkcie.
import math

x = int(input('Zadaj vstupne cislo'))
z = int(input('Zadaj konecne cislo'))

for i in range(x,z+1):
    y = math.sqrt (i)
    print(round(y,2))