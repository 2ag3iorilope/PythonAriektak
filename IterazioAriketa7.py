import math

Zenbakia = int(input("Sartu zenbaki oso bat 1 baino handiago dena: "))

if Zenbakia > 1:
    lehena_da = True 
    
    for i in range(2, int(math.sqrt(Zenbakia)) + 1):
        if Zenbakia % i == 0: #Modulua zero badu  lehena ez da
            lehena_da = False 
            break 
    
    if lehena_da:
        print("{} Zenbaki lehena da.".format(Zenbakia))
    else:
        print("{} Ez da zenbaki lehena.".format(Zenbakia))
else:
    print("Zenbakiak 1 baino handiago izan behar du")
