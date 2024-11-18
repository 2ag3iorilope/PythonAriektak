import math  # Math inportatu Pi erabiltzeko

# Erabiltzaileari galdetu
aukera = input("¿Zeinen area kalkulatu nahi duzu? (trianguloa/zirkulua): ").strip().lower()

if aukera == "trianguloa":
    oinarria = float(input("Sartu trianguluaren oinarrria: "))
    altuera = float(input("Sartu trianguluaren altuera: "))
    
    # Kalkulatu
    azalera_triangulo = (oinarria * altuera) / 2
    
    print("Trianguluaren azalera: " + str(azalera_triangulo) + " da")

elif aukera == "zirkulua":
    erradio = float(input("Sartu zirkuluaren erradioa: "))
    
    # Kalkulatu
    azalera_zirkulu = math.pi * (erradio ** 2)
    
    print("Zirkuluaren Azalera: " + str(azalera_zirkulu) + " da.")

else:
    print("Aukera desegokia. Aukerak Trianguloa eta Zirkulua dira.")
