# uloha 6
x = int(input('Zadaj cele cislo: '))

if x % 4 == 0:
    print('Cislo', x, 'je delitelne styrmi.')
elif x % 7 == 0:
    print('Cislo', x, 'je delitelne siedmimi.')
else:
    print('Cislo', x, 'nie je delitelne ani styrmi, ani siedmimi.')
