import random
import time

def zenbaki_asmatzea():
    print("Ongi etorri zenbaki asmatzeko jokoan!")

    Denbroa_hobe = float('inf')  

    while True:
        try:
            asmatu_egon_aldiz = int(input("Zenbat eragiketa asmatu behar dituzu? (Adib. 5): "))
            if asmatu_egon_aldiz <= 0:
                print("Mesedez, idatzi zenbaki positibo bat.")
                continue
            break
        except ValueError:
            print("Mesedez, idatzi zenbaki osoko balio bat.")

    print("Sartu zenbaki bat 0 eta 100 artean, eta egiaztatuko dugu asmatu duzun!")

    asmatuak = 0  
    guztira_saiakerak = 0  

    while asmatu_egon_aldiz > 0:
        zbki_ezkutua = random.randint(1, 100)
        print("\nZenbaki bat sortu dut 1 eta 100 artean")

        saiakerak = 0
        denbora_hasi = time.time()
        while True:
            try:
                zbki = input("Sartu bi zenbaki (tartez bananduta): ")
                zbki1, zbki2 = map(int, zbki.split())

                if zbki1 < 0 or zbki1 > 100 or zbki2 < 0 or zbki2 > 100:
                    print("Errorea: Sartu zenbakiak 0 eta 100 artean!")
                    continue  

             
                saiakerak += 1  
                if zbki1 == zbki_ezkutua or zbki2 == zbki_ezkutua:
                    asmatuak += 1
                    print("Zorionak! "+ str(asmatuak)+"/"+str(asmatu_egon_aldiz)+"  asmatu duzu!")
                    guztira_saiakerak += saiakerak
                    denbora_bukatu = time.time()
                    break  
                else:
                    print("Ez duzu asmatu. Saiatu berriro!")
            except ValueError:
                print("Mesedez, zenbaki bi sartu.")

       
        denbora_sesioa = denbora_bukatu - denbora_hasi
        if denbora_sesioa < Denbroa_hobe:
            Denbroa_hobe = denbora_sesioa

        asmatu_egon_aldiz -= 1

        if asmatu_egon_aldiz > 0:
            jaraitu = input("Beste saiakera bat egin nahi al duzu? (bai/ez): ")
            if jaraitu.lower() != 'bai':
                break

   
    print("\nZorionak! "+ str(asmatuak)+" aldiz asmatu duzu!")
    print("Saio guztietan "+ str(guztira_saiakerak)+ " saiakera egin dituzu.")
    print("Guztira " + str(denbora_bukatu - denbora_hasi) + " segundo behar izan dituzu.")
    print("Denbora minimoa: " + str(Denbroa_hobe) + " segundo.")

zenbaki_asmatzea()
