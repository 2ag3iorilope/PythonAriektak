def Irakurri_Ordenatua(n, izena):
    print("{} zenbaki oso ordenatuta sartu '{}' egiteko:".format(n, izena))
    return [int(input("Zenbakia {}: ".format(i+1))) for i in range(n)]

def Serieak_Fusionatu(seriea1, seriea2):
    fusionatua = []
    i, j = 0, 0
 
    while i < len(seriea1) and j < len(seriea2):
        if seriea1[i] <= seriea2[j]:
            fusionatua.append(seriea1[i])
            i += 1
        else:
            fusionatua.append(seriea2[j])
            j += 1
   
    fusionatua.extend(seriea1[i:])
    fusionatua.extend(seriea2[j:])
    return fusionatua


seriea1 = Irakurri_Ordenatua(10, "1. Seriea")
seriea2 = Irakurri_Ordenatua(10, "2. Seriea")

serie_fusionatuta = Serieak_Fusionatu(seriea1, seriea2)


print("Serie fusionatua ordenatuta:", serie_fusionatuta)
