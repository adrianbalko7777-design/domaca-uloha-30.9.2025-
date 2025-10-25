# Naprogramuj funkciu, ktorá vypíše čísla od 1-N, N je vstupný parameter  a.    Pod seba b.    za sebou, pričom čísla budú oddelené čiarkou

x = int(input('Zadaj vstupne cislo'))

for i in range(1,x+1):
    print(i)

for i in range(1,x+1):
    if i < x:
        print(i, end=', ')
    else:
        print(i)