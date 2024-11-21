limitea = int(input("Sartu balio limitea: "))

if limitea <= 0:
    print("Balore limiteak positiboa izan behar du.")
else:
    batura = 0
    while batura <= limitea:
        zenbaki_sartu = int(input("Sartu zenbaki oso bat: "))
        batura += zenbaki_sartu
    print("Sartutako zenbakien baturak " + str(limitea) + " muga gainditu du. Guztizko batura " + str(batura) + " da.")
