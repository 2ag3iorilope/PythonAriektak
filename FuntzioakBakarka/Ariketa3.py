def KalkulatuZKH(z1,z2):
    while z2 != 0:
        z1, z2 = z2, z1 % z2
    return z1

emaitza = KalkulatuZKH(45,33)
print( "Sartutako zenbakien ZKH da: " + str(emaitza))