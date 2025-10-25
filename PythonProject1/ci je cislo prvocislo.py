# ideme zistit ci je cislo prvocilo pomocou
number = int(input('Zadaj cislo x: '))
cn = 0
for delitel in range(2,number):   #for delitel in range(2,int(number**0.5+1):
    if number % delitel == 0:
        cn += 1
if cn == 0:
    print('Je to prvocilo ')
else:
    print('Nieje to prvocilo ')