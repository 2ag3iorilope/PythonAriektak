import random

puntuazio_jokalari_1 = 0
puntuazio_jokalari_2 = 0

def botatze_dadoa():
    return random.randint(1, 6)

print("Bien arteko dado jokoan parte hartu duzu. Dadoak botatzen dituzu!")

while True:
    input("Sakatu Enter jokalariek dadoak botatzeko...")

    dadoa_jokalari_1 = botatze_dadoa()
    dadoa_jokalari_2 = botatze_dadoa()

    print("Jokalari 1-en dadoa: " + str(dadoa_jokalari_1))
    print("Jokalari 2-ren dadoa: " + str(dadoa_jokalari_2))

    puntuazio_jokalari_1 += dadoa_jokalari_1
    puntuazio_jokalari_2 += dadoa_jokalari_2

    print("Orain arteko puntuazioa: ")
    print("Jokalari 1: " + str(puntuazio_jokalari_1))
    print("Jokalari 2: " + str(puntuazio_jokalari_2))

   
    print("Jokoarekin jarraitu nahi duzu? (bai/ez)")
    erantzunaJK1 = input("Jokalaria 1: ").lower()
    erantzunaJK2 = input("Jokalaria 2: ").lower()

   
    if erantzunaJK1 == "ez" and erantzunaJK2 == "ez":
        print("Jokoaren amaiera! Azken puntuazioa:")
        print("Jokalari 1: " + str(puntuazio_jokalari_1))
        print("Jokalari 2: " + str(puntuazio_jokalari_2))
        
       
        if puntuazio_jokalari_1 > 20 and puntuazio_jokalari_2 > 20:
            print("Inork ez du irabazi! Biak puntuazio-muga gainditu dute.")
        elif puntuazio_jokalari_1 > 20:
            print("Irabazlea: Jokalari 2! (Jokalari 1 muga gainditu du)")
        elif puntuazio_jokalari_2 > 20:
            print("Irabazlea: Jokalari 1! (Jokalari 2 muga gainditu du)")
        elif puntuazio_jokalari_1 > puntuazio_jokalari_2:
            print("Irabazlea: Jokalari 1!")
        elif puntuazio_jokalari_2 > puntuazio_jokalari_1:
            print("Irabazlea: Jokalari 2!")
        else:
            print("Berdinketa izan da!")
        break

    
    elif puntuazio_jokalari_1 >= 20 or puntuazio_jokalari_2 >= 20:
        print("Jokoaren amaiera! Azken puntuazioa:")
        print("Jokalari 1: " + str(puntuazio_jokalari_1))
        print("Jokalari 2: " + str(puntuazio_jokalari_2))
        
 
        if puntuazio_jokalari_1 > 20 and puntuazio_jokalari_2 > 20:
            print("Inork ez du irabazi! Biak puntuazio-muga gainditu dute.")
        elif puntuazio_jokalari_1 > 20:
            print("Irabazlea: Jokalari 2! (Jokalari 1 muga gainditu du)")
        elif puntuazio_jokalari_2 > 20:
            print("Irabazlea: Jokalari 1! (Jokalari 2 muga gainditu du)")
        elif puntuazio_jokalari_1 > puntuazio_jokalari_2:
            print("Irabazlea: Jokalari 1!")
        elif puntuazio_jokalari_2 > puntuazio_jokalari_1:
            print("Irabazlea: Jokalari 2!")
        else:
            print("Berdinketa izan da!")
        break
    else:
        print("Jokoa jarraitzen da!")
