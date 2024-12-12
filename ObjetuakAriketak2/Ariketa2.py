class TintaAmaitutaException(Exception):
    pass

class Papel:
    def __init__(self):
        self.testua = ""

    def Idatzi(self, testua):
        self.testua += testua

    def __str__(self):
        return self.testua


class Boligrafo:
    def __init__(self, Tinta_Kop):
        self.Tinta_Kop = Tinta_Kop

    def Idatzi(self, testua, papel):
        if len(testua) > self.Tinta_Kop:
            raise TintaAmaitutaException("Ez dago tintarik.")
        
        papel.Idatzi(testua)
        self.Tinta_Kop -= len(testua)
        

papel = Papel()
boligrafo = Boligrafo(50)  

try:
    boligrafo.Idatzi("Testuaa. ", papel)
    boligrafo.Idatzi("Testu gehiagooo.", papel)
    print(papel)  
    print("Geratzen den tinta:", boligrafo.Tinta_Kop)
except TintaAmaitutaException as e:
    print(e)