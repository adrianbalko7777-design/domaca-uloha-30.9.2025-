# 13 naprogramuj funkciu, ktorá sčíta všetky párne čísla od 1-N


def sucet_od_1_do_N(N):
    sucet = 0
    x = 0
    for i in range(1, N + 1):
        if i % 2 == 0:
            x += i
        sucet += x
    return x

# hlavny program
N = int(input("Zadaj N: "))
print("Sucet cisel od 1 po", N, "je", sucet_od_1_do_N(N))