import random

Zenbaki1 = random.randint(11, 99)
Zenbaki2 = random.randint(11, 99)

emaitza_ongi = Zenbaki1 * Zenbaki2

emaitza_sartu = int(input("¿Zein da " + str(Zenbaki1) + " * " + str(Zenbaki2) + " ren erantzuna? "))

desberdintasuna = abs(emaitza_sartu - emaitza_ongi)

if emaitza_sartu == emaitza_ongi:
    print("¡Asmatu duzu!")
elif desberdintasuna <= (0.1 * emaitza_ongi):
    print("Zure erantzuna balio zuzenaren % 10aren barruan dago.")
elif desberdintasuna <= (0.3 * emaitza_ongi):
    print("Zure erantzuna balio zuzenaren % 30aren barruan dago.")
else:
    print("Erantzun okerra. Emaitza zuzena " + str(emaitza_ongi) + ".")
