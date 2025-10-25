#Naprogramuj funkciu, ktorá pre dané x z intervalu <1,20> bude počítať funkčné hodnoty podľa predpisu y= (x**2-1)/(x-3) .
# Uvedomte si, že nulou sa nemôže deliť.
# T.j. pre x=3 funkcia nie je definovaná

for i in range(1,20+1):
    if i  == 3:
        print('funkcia nieje definovana')
    else:
        y = (i ** 2 - 1) / (i - 3)
        (print(i,(round(y,4))))
