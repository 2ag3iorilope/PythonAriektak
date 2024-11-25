import random

while True:
    input("Sakatu enter ausazko zenbakiak sortzeko: ")
    zenbakia = random.randint(1, 6)
    print("Ausazko Zenbakia: " + str(zenbakia))
    
    erantzuna = input("Beste ausazko zenbaki bat lortu nahi duzu? (bai/ez): ").lower()
    if erantzuna != "bai":
        print("Agur!")
        break
