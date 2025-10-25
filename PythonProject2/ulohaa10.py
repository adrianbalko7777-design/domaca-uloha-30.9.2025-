# vypíš čísla od 1-N odzadu, za sebou. Ak N=5 , výsledok by mal byť: 5,4,3,2,1

x = int(input("zadaj cislo N: "))

for i in range(x,1,-1):
    print(i)
print(1)