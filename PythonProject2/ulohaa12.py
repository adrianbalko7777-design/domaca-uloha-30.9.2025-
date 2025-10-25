# Naprogramuj funkciu , ktorá sčíta dokopy čísla od 1 do N. (N -parameter funkcie)
import math

# uloha ktoru som nevedel odpisana z internetu
def sucet_od_1_do_N(N):
    sucet = 0
    for i in range(1, N + 1):
        sucet += i
    return sucet

# hlavny program
N = int(input("Zadaj N: "))
print("Sucet cisel od 1 po", N, "je", sucet_od_1_do_N(N))