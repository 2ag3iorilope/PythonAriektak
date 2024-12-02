def BatDatoz(tupla1,tupla2):
     return sum(1 for x, y in zip(tupla1, tupla2) if x == y)
 

tupla1= (1,2,3,4,5,6,7,8)
tupla2=(9,10,7,4,5,4,3,2)

emaitza = BatDatoz(tupla1,tupla2)

print("Sartutako tuplen koinzidentzia kopurua : " + str(emaitza) )

    