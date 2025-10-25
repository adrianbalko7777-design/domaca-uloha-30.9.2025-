#Naprogramuj funkciu, ktorá vypíše čísla od 1 po N a ich druhé mocniny. Pričom N je argumentom funkcie.

import math
x = int(input('Zadaj vstupne cislo'))
for i in range(1,x+1):
    y = int(math.pow(i,2))
    print(i,y)
