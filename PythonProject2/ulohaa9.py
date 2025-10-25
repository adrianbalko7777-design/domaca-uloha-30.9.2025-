# Vypíš všetky nepárne čísla od z do k (kde z-zaciatok, k - koniec) Napr.pre z=6 a pre k=10 sa vypíše 7,9

x = int(input("Zadaj zaciatocne cislo: "))
y = int(input("zadaj konecne cislo: "))

for i in range(x,y):
    if i % 2 == 1:
        print(i)