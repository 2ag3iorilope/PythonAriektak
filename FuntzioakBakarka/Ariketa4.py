def KalkulatuMKT(z1,z2):
    
    def KalkulatuZKH(x, y):
        while y:
            x, y = y, x % y
        return x
    
    
    
    return abs(z1 * z2) // KalkulatuZKH(z1, z2)

z1= 34
z2= 45
emaitza = KalkulatuMKT(z1,z2)

print("Sartutako zenbakien MKt da: " + str(emaitza))