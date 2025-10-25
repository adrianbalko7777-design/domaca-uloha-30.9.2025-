# ideme spocitat vsetky cisla v intervale ktore siu parne hochu
a = int(input('zadaj vrchnu hodnotu intervalu'))
b = int(input('zadaj spodnu hodnotu intervalu'))
x = 0
for i in range(b,a):
    if i % 2 == 0:
        x = x + 1
print('pocet parnych cisel v tomto intervle je',x)

