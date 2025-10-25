# Napíšte funkciu, ktorá zistí, či je dané číslo prvočíslom
# ktore cisl z intervalu su prvocisla

x = int(input('Zadaj cislo x: '))
cn = 0
for delitel in range(2,x):   #for delitel in range(2,int(number**0.5+1):
    if x % delitel == 0:
        cn += 1
if cn == 0:
    print('Je to prvocilo ')
else:
    print('Nieje to prvocilo ')
