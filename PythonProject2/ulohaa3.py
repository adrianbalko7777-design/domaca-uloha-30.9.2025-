#Naprogramuj funkciu, ktorá vypíše každé druhé číslo, počínajúc čislom 5 až po N

x = int(input('Zadaj vstupne cislo'))
for i in range(5,x+1,2):
    print(i)