import random

def txanponJokoa():
    
    txanponak = int(input("Zenbat txanpon dituzu hasteko? "))  
    if txanponak <= 0:
        print("Txanpon kopurua ezin da 0 edo txikiagoa izan.")
        return

    while txanponak > 0:
        print("Zure saldoa: " + str(txanponak) + " txanpon")  
        txanponak -= 1  

        zenbakiak = [random.randint(1, 6) for _ in range(3)]
        print("Ausazko hiru zenbaki:", zenbakiak)

        if len(set(zenbakiak)) == 1:
            print("Hiru zenbaki berdinak dira! Zure saria: 5 txanpon")
            txanponak += 5  
        elif len(set(zenbakiak)) == 2:
            print("Bi zenbaki berdinak dira! Zure saria: 2 txanpon")
            txanponak += 2  
        else:
            print("Ez daude berdinak diren zenbakiak. Ezin duzu ezer irabazi.")

        print("Saldoa orain: " + str(txanponak) + " txanpon")  

        if txanponak == 0:
            print("Ez duzu gehiago jokatzerik. Jokoaren amaiera!")
            break

        erantzunaJK = input("Jokatzen jarraitu nahi duzu? (bai/ez): ").lower()
        if erantzunaJK == "ez":
            break

    print("Jokoaren amaiera! Lortutako saldoa: " + str(txanponak) + " txanpon") 
    
if __name__ == "__main__":
    txanponJokoa()
