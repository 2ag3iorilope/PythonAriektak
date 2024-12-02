def kalkulatuZenbakiHaundiena(z1, z2):
    if z1 > z2:
        return z1
    elif z2 > z1:
        return z2
    else:
        return "Zenbakiak berdinak dira"
 
z1=5 
z2=3

emaitza = kalkulatuZenbakiHaundiena(z1,z2)
print(emaitza)