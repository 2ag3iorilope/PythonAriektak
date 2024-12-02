def KalkulatuHaundiena(*zenbakiak):

    if not zenbakiak:
      return("Ez duzu zenbakirik sartu")
      
    return max(zenbakiak)

emaitza = KalkulatuHaundiena(1,2,3,4,5,6,7,89)
print ("Sartu duzun zenbaki handiena : " + str(emaitza))
    