# uloha 3
a = int(input('Zadaj dolnu hranicu intervalu a: '))
b = int(input('Zadaj hornu hranicu intervalu b: '))
x = int(input('Zadaj cislo x: '))

if a <= x <= b:
    print('Cislo', x, 'patri do intervalu <', a, ',', b, '>.')
else:
    print('Cislo', x, 'nepatri do intervalu <', a, ',', b, '>.')