#program ktory vypocita faktorial cisla
a = int(input('zadaj vrchnu hodnotu intervalu'))
b = int(input('zadaj spodnu hodnotu intervalu'))
x = 0
for i in range(b,a+1):
    x = x + i
print(x)