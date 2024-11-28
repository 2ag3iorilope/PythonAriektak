def IrakurriZenbakiak():
    
    zenbakiak = tuple(int(input("Sartu zenbakia {}: ".format(i+1))) for i in range(10))
    return zenbakiak

def Erakutsi_Ordenean(zenbakiak):
    Emaitza = []
    n = len(zenbakiak)
    
   
    for i in range((n + 1) // 2):
        Emaitza.append(zenbakiak[i]) 
        if i != n - i - 1:  
            Emaitza.append(zenbakiak[n - i - 1]) 

    return tuple(Emaitza)  

# Ejecución directa
zenbakiak = IrakurriZenbakiak()
Emaitza = Erakutsi_Ordenean(zenbakiak)
print("Zenbakiak Ordenean:", Emaitza)
