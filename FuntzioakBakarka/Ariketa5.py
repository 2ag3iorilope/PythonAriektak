def GehituBakoitiak(kopurua):
    gehiketa = 0
    kontagailua = 1
    
    for i in range(kopurua):
        gehiketa += kontagailua
        kontagailua += 2  
    return gehiketa

kopurua = 12
emaitza = GehituBakoitiak(kopurua)
print(emaitza)
