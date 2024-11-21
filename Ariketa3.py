ZenbakiKop = int(input ("Zenbat zenbaki sartu nahi dituzu?"))

if ZenbakiKop > 0:
    lehenena = int(input("Sartu lehen zenbakia: "))
    
    
    for i in range(2, ZenbakiKop + 1):
        momentukozenbakia = int(input("Sartu zenbakia {}: ".format(i)))
        
       
        if momentukozenbakia <= lehenena:
            print("Zenbaki hau ez da lehengo baino handiagoa.")
else:
    print("Zenbaki kopurua 0 baino handiagoa izan behar du.")