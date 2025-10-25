# pocitame kolko cifier ma cislo
number = int(input('Zadaj cislo x: '))
scitovanie_cifier = 0

while number != 0:
    cifra = number%10
    scitovanie_cifier += cifra
    number = number // 10

print(scitovanie_cifier)