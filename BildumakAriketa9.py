def sortu_zerrenda():
    n = int(input("Zenbat hitz sartu nahi dituzu zerrendan? "))
    zerrenda = [input("Sartu hitza {}: ".format(i + 1)) for i in range(n)]
    return zerrenda

def ezabatu_hitza(zerrenda):
    hitza = input("Sartu ezabatu nahi duzun hitza: ")
    if hitza in zerrenda:
        zerrenda.remove(hitza)
        print("'{}' hitza zerrendatik kendu da.".format(hitza))
    else:
        print("'{}' hitza ez dago zerrendan.".format(hitza))
    return zerrenda


hitz_zerrenda = sortu_zerrenda()


hitz_zerrenda = ezabatu_hitza(hitz_zerrenda)


print("Eguneratutako zerrenda:", hitz_zerrenda)
