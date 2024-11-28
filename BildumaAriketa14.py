def sortu_eta_ordenatu_zerrenda():
 
    n = int(input("Zenbat hitz sartu nahi dituzu zerrendan? "))
    zerrenda = [input("Sartu hitza {}: ".format(i + 1)) for i in range(n)]


    zerrenda.sort()
    return zerrenda

# Programa exekutatu
print("Sortu eta ordenatu zerrenda:")
hitz_zerrenda = sortu_eta_ordenatu_zerrenda()

# Emaitzak erakutsi
print("Zerrenda alfabetikoki ordenatuta:", hitz_zerrenda)
