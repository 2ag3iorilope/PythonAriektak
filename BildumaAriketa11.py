def sortu_zerrenda():
    n = int(input("Zenbat hitz sartu nahi dituzu zerrendan? "))
    zerrenda = [input("Sartu hitza {}: ".format(i + 1)) for i in range(n)]
    return zerrenda

def sortu_zerrenda_berdina_baina_itzulia(lista):
    itzulia = lista[::-1] 
    return itzulia


hitz_zerrenda = sortu_zerrenda()


hitz_zerrenda_itzulia = sortu_zerrenda_berdina_baina_itzulia(hitz_zerrenda)


print("Hasierako zerrenda:", hitz_zerrenda)
print("Zerrenda itzulia:", hitz_zerrenda_itzulia)
